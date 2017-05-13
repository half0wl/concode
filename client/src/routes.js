import WelcomeComponent from 'components/Welcome'
import LoginComponent from 'components/Login'
import HelloComponent from 'components/Hello'

export default [
  {
    path: '/',
    component: WelcomeComponent
  },
  {
    path: '/login',
    name: 'login',
    meta: {auth: false},
    component: LoginComponent
  },
  {
    path: '/hello/:name',
    component: HelloComponent
  }
]
