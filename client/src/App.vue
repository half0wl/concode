<template>
  <div id="app" v-if="$auth.ready()">
    <AppHeader></AppHeader>
    <router-view></router-view>
    <div>
      <h3>Change language</h3>
      <button @click="setLang(lang)" v-for="lang in locales" :disabled="isLang(lang)">{{ $t('locales.'+ lang) }}</button>
    </div>
    <hr>
    <div>
      <button @click="increment">{{ $tc('messages.counter', countPlural, { n: $store.state.count }) }}</button>
    </div>
    <router-link class="link" v-if="!$auth.check()" to="/login/github">{{ $t('links.login') }}</router-link>
    <span v-if="$auth.check()">Hello {{ $auth.user().username }} | <a class="link" v-on:click="logout()">{{ $t('links.logout') }}</a></span>
  </div>
</template>

<script>
import store from 'store'
import { mapActions, mapGetters } from 'vuex'
import AppHeader from 'components/AppHeader'
export default {
  store,
  data () {
    return {
      context: 'app context'
    }
  },
  components: {
    AppHeader
  },
  computed: mapGetters([
    'countPlural'
  ]),
  methods: {
    ...mapActions([
      'increment'
    ]),
    onLangClick (lang) {
      this.setLang(lang) // mixin method
      this.increment() // store action
    },
    logout () {
      this.$auth.logout({
        makeRequest: false,
        success () {
          document.cookie = 'token=;expires=Thu, 01 Jan 1970 00:00:01 GMT;'
          console.log('success ' + this.context)
        },
        error () {
          console.log('error ' + this.context)
        }
      })
    }
  },
  created: function fetch () {
    this.$auth.fetch({
      success () {
        console.log('success ' + this.context)
      },
      error () {
        console.log('error ' + this.context)
      }
    })
  }
}
</script>

<style lang="scss">
@import "styles/theme/index";

html {
  height: 100%;
}

body{
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

#app {
  text-align: center;
}

.icon-logo {
  margin-bottom: 2.5rem;
}
</style>
