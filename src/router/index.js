import Vue from 'vue'
import Router from 'vue-router'
import AutomobileForm from '@/components/AutomobileForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Automobile Form',
      component: AutomobileForm
    }
  ]
})
