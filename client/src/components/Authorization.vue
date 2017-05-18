<template>
    <div v-show="!code || !type" class="auth">
        <p @click="social('github')">Try this: <span id="jwt">{{ this.$auth.token() }}</span></p>
        <span v-if="$auth.check">{{ $auth.user() }}</span>
    </div>
</template>

<script>
export default {
  data () {
    return {
      context: 'auth context',
      code: this.$route.query.code,
      type: this.$route.params.type
    }
  },
  methods: {
    social (type) {
      this.$auth.oauth2({
        code: true,
        provider: type || this.type,
        params: {
          code: this.code
        }
      })
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
        success: function (res) {
          console.log('Success!' + this.context)
          document.getElementById('jwt').text = res.token
        },
        error: function (res) {
          console.log('Fail... ' + this.context + ' ' + res.data)
        },
        redirect: {path: '/account'}
        // etc
      })
    }
  }
}
</script>

<<style lang="stylus">
</style>
