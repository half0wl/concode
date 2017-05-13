/* eslint-disable no-unused-vars */
import VueRouter from 'vue-router'
import routes from 'src/routes'

export default {
  router: null,
  install (Vue) {
    const router = new VueRouter({
      routes,
      hashbang: false,
      linkActiveClass: 'active',
      mode: 'history'
    })

    Vue.mixin({
      beforeCreate () {
        if (this.$root === this) {
          this.$options.router = router
        }
      }
    })

    Vue.use(VueRouter)
  }
}
