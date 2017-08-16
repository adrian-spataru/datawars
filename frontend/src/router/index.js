import Vue from 'vue'
import VueRouter from 'vue-router'
import Hello from '@/components/Hello'
import Leaderboard from '@/components/Leaderboard'
import Login from '@/components/Login'
Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'leaderboard',
      component: Leaderboard,
      meta: {auth: true}
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {auth: true}

    }

  ]
})
