import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Leaderboard from '@/components/Leaderboard'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'leaderboard',
      component: Leaderboard 
    }
  ]
})
