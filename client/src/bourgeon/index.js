/* eslint-disable no-unused-vars */
import Router from 'bourgeon/router'
import I18n from 'bourgeon/i18n'
import VueResource from 'vue-resource'

export default {
  install (Vue, options) {
    Vue.use(Router)
    Vue.use(I18n, options.locales)
    Vue.use(VueResource)
  }
}
