<template>
  <div id="content" class="login">
    <h1>{{ $t('links.login') }}</h1>
    <div v-show="!code || !type">
      <button v-on:click="social('github')">Sign in with GitHub</button>
    </div>
    <div v-show="code && type">
      Verifying {{ type }} code&hellip;
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      context: 'oauth2 context',
      code: this.$route.query.code,
      type: this.$route.params.type,
      error: null
    }
  },
  mounted () {
    console.log(this)
    if (this.code) {
      this.$auth.oauth2({
        code: true,
        provider: this.type,
        params: {
          code: this.code
        },
        body: {
          provider: this.type,
          code: this.code
        },
        success: function (res) {
          console.log('success ' + this.context)
        },
        error: function (res) {
          console.log('error ' + this.context)
          res.status(400).send('Something went wrong')
        },
        redirect: {
          name: 'dashboard'
        }
      })
    }
  },
  methods: {
    social (type) {
      this.$auth.oauth2({
        provider: type || this.type
      })
    }
  }
}
</script>

<style lang="scss">
@import "./../styles/theme/variables";
h1 {
  color: $accent;
}

form input[type] {
  display: inline-block;
  width: 100%;
}

[dir="ltr"] label {
  text-align: left;
}
</style>