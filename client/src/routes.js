import WelcomeComponent from 'components/Welcome'
import LoginComponent from 'components/Login'
import HelloComponent from 'components/Hello'

export default [
  {
    path: '/',
    component: WelcomeComponent
  }, {
    path: '/login',
    name: 'login',
    meta: {auth: false},
    component: LoginComponent
  }, {
    path: '/login/:type',
    name: 'oauth2-type',
    component: LoginComponent
  }, {
    path: '/hello/:name',
    component: HelloComponent
  }, {
    path: '/404',
    name: 'error-404',
    component: require('./components/pages/404.vue')
  }, {
    path: '/403',
    name: 'error-403',
    component: require('./components/pages/403.vue')
  }, {
    path: '/502',
    name: 'error-502',
    component: require('./components/pages/502.vue')
  }, {
    path: '/teapot',
    name: 'error-418',
    component: require('./components/pages/418.vue')
  }, {
    path: '*',
    component: require('./components/pages/404.vue')
  }
]
