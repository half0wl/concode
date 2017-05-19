<template>
    <div class="auth">
        <div v-show="!code || !type">
            <p @click="social('github')">Try this: <span id="jwt">{{ this.$auth.token() }}</span></p>
            <span v-if="$auth.check">{{ $auth.user() }}</span>
        </div>
        <div v-show="code && type">
            <div style="word-wrap:break-word;">{{ token === '' ? 'select token' : (token ? token : 'no token set') }}</div>
            <ul>
                <li><a v-on:click="setToken()" href="javascript:void(0);">Test default token</a></li>
                <li><a v-on:click="setToken('other')" href="javascript:void(0);">Test other token</a></li>
                <li><a v-on:click="setToken('default')" href="javascript:void(0);">Test admin token</a></li>
                <li><a v-on:click="clearToken()" href="javascript:void(0);">Test cache clear</a></li>
                <li><a v-on:click="setDudToken()" href="javascript:void(0);">Test dud</a></li>
                <li><a v-on:click="networkDrop('other')" href="javascript:void(0);">Test network drop</a></li>
            </ul>
        </div>
        <form v-on:submit.prevent="register()">
            <input type="hidden" v-model="data.body.username">
            <input type="hidden" v-model="data.body.password">
        </form>
    </div>
</template>

<script>
export default {
  data () {
    return {
      context: 'auth context',
      code: this.$route.query.code,
      type: this.$route.params.type,
      error: null,
      token: '',
      data: {
        body: {
          username: '',
          password: '',
          avatar: null
        }
      }
    }
  },
  methods: {
    setToken (name) {
      if (window.localStorage) {
        window.localStorage.setItem('token', this.token)
      }
      this.token = this.$auth.token(name)
    },
    clearToken () {
      window.localStorage.removeItem('other_auth_token')
      window.localStorage.removeItem('default_auth_token')
      window.cookie.delete.call(this.$auth, 'other_auth_token')
      window.cookie.delete.call(this.$auth, 'default_auth_token')
      console.log('Tokens removed')
    },
    setDudToken () {
      window.localStorage.setItem('other_auth_token', 'nil')
      window.localStorage.setItem('default_auth_token', 'nil')
      window.cookie.set.call(this.$auth, 'other_auth_token', 'nil')
      window.cookie.set.call(this.$auth, 'default_auth_token', 'nil')
    },
    networkDrop () {
      this.http.options.root = 'https://does.not.exist.com//api/v1'
      console.log('http.options.root changed to https://does.not.exist.com/api/v1')
    },
    social (type) {
      this.$auth.oauth2({
        provider: type || this.type,
        params: {
          provider: this.provider
        }
      })
    },
    isQuotaExceeded: function (exception) {
      let quotaExceeded = false
      if (exception) {
        if (exception.code) {
          switch (exception.code) {
            case 22:
              quotaExceeded = true
              break
            case 1014:
              if (exception.name === 'NS_ERROR_DOM_QUOTA_REACHED') {
                quotaExceeded = true
              }
              break
          }
        } else if (exception.number === -2147024882) {
          quotaExceeded = true
        }
      }
      return quotaExceeded
    },
    storage: function () {
      const uid = new Date()
      let storage
      let result
      try {
        (storage = window.localStorage).setItem(uid, uid)
        result = storage.getItem(uid) === uid
        storage.removeItem(uid)
        return result && storage
      } catch (exception) {
        if (this.isQuotaExceeded(exception)) {
          console.log('Your local storage is full. :(')
        }
      }
    }
  },
  mounted () {
    if (this.code) {
      this.$auth.oauth2({
        code: true,
        provider: 'github',
        params: {
          code: this.code
        },
        body: {
          provider: 'github',
          code: this.code
        },
        success (res) {
          console.log('Success!' + this.context)
          this.token = res.data.token
          document.getElementById('jwt').text = this.token
          document.cookie = 'token=' + this.token
          if (this.storage) {
            console.log('localStorage enabled')
            this.storage.setItem('token', this.token)
          } else {
            console.log('localStorage disabled')
          }
        },
        error (res) {
          console.log(this.error + ' ' + this.context + ' ' + res)
          this.error = res.data
        },
        redirect: {name: 'account'}
        // etc
      })
    }
    if (this.storage) {
      console.log('localStorage enabled')
      this.storage.setItem('token', this.token)
    } else {
      console.log('localStorage disabled')
    }
  }
}
</script>

<<style lang="stylus">
</style>
