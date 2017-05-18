// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import 'es6-promise/auto'
import Bourgeon from 'bourgeon'
import VueRouter from 'vue-router'
import App from './App'

Vue.use(Bourgeon, {
  locales: ['en', 'zh', 'fr']
})

Vue.http.options.root = 'https://concode-api.herokuapp.com'
Vue.router = new VueRouter()

Vue.use(require('vue-auth'), {
  auth: require('vue-auth/drivers/auth/bearer.js'),
  http: require('vue-auth/drivers/http/vue-resource.1.x.js'),
  router: require('vue-auth/drivers/router/vue-router.2.x.js'),
  rolesVar: 'type',
  loginData: { url: 'auth/callback', method: 'POST', redirect: '/', fetchUser: false },
  fetchData: {url: 'authorization', method: 'GET'},
  githubData: { url: 'auth/social/jwt/', method: 'POST', redirect: '/' },
  githubOauth2Data: {
    url: 'https://github.com/login/oauth/authorize',
    redirect: function () { return this.options.getUrl() + '/authorization' },
    // redirect: function () { return 'https://concode-api.herokuapp.com/authorization' },
    clientId: 'f011549ce875a82ec3a1',
    scope: 'email'
  }
})

App.router = Vue.router

/* eslint-disable no-new */
new Vue({
  render: h => h(App),
  watch: {
    lang: function (val) {
      Vue.config.lang = val
    }
  }
}).$mount('#app')
