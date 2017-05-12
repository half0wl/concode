<template>
  <div id="app">
    <img class="logo" src="./assets/logo.png">
    <router-view></router-view>
    <div>
      <h3>Change language</h3>
      <button @click="setLang(lang)" v-for="lang in locales" :disabled="isLang(lang)">{{ $t('locales.'+ lang) }}</button>
    </div>
    <hr>
    <div>
      <button @click="increment">{{ $tc('messages.counter', countPlural, { n: $store.state.count }) }}</button>
    </div>
    <router-link v-if="!$auth.check()" to="/hello/concode">{{ $t('links.login') }}</router-link>
    <a v-if="$auth.check()" v-on:click="$auth.logout()">logout</a>
  </div>
</template>

<script>
import store from 'store'
import { mapActions, mapGetters } from 'vuex'
export default {
  store,
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
    }
  }
}
</script>

<style lang="stylus">
@import "../node_modules/typus" // base styles
@import "styles/theme"

body
  +above(320px) // rupture
    font-size 1.6rem

#app
  align() // jeet
  text-align center

.icon-logo
  margin-bottom 2.5rem
</style>
