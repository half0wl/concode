// jshint esversion:6
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Bourgeon from 'bourgeon'
import VueRouter from 'vue-router'
import App from './App'

Vue.use(Bourgeon, {
  locales: ['en', 'zh', 'fr']
})

Vue.http.options.root = 'https://api-demo.websanova.com/api/v1'
Vue.router = new VueRouter()

Vue.use(require('vue-auth'), {
  auth: require('vue-auth/drivers/auth/bearer.js'),
  http: require('vue-auth/drivers/http/vue-resource.1.x.js'),
  router: require('vue-auth/drivers/router/vue-router.2.x.js'),
  rolesVar: 'type'
})

/* eslint-disable no-new */
new Vue({
  render: h => h(App),
  watch: {
    lang: function (val) {
      Vue.config.lang = val
    }
  }
}).$mount('#app')
