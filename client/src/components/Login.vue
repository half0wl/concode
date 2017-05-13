<template>
  <div class="login">
    <h1>{{ $t('links.login') }}</h1>
    <form v-if="!$auth.check()" v-on:submit.prevent="login()">
        <label>Username 
            <input type="text" v-model="data.body.username">
        </label>
        <label>Password 
            <input type="password" v-model="data.body.password">
        </label>
        <button role="submit">{{ $t('links.login') }}</button>
        <p v-show="error" style="color:red; word-wrap:break-word;">{{ error }}</p>
    </form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      context: 'login context',
      data: {
        body: {
          username: 'admin',
          password: 'secret'
        },
        rememberMe: false,
        fetchUser: true
      },
      error: null
    }
  },
  mounted () {
    console.log(this.$auth.redirect())
    // Can set query parameter here for auth redirect or just do it silently in login redirect.
  },
  methods: {
    login () {
      var redirect = this.$auth.redirect()
      this.$auth.login({
        body: this.data.body,
        rememberMe: this.data.rememberMe,
        redirect: {
          name: redirect ? redirect.from.name : 'hello'
        },
        fetchUser: this.data.fetchUser,
        success () {
          console.log('success ' + this.context)
        },
        error (res) {
          console.log('error ' + this.context)
          this.error = res.data.msg
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="stylus" scoped>
h1
  color accent
form input[type]
  display inline-block
  width 100%
[dir="ltr"] label
  text-align left
</style>