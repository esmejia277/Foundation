import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Colleges from '@/components/Colleges'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../components/Home.vue')
      
    },
    {
      path: '/programas/haciendo-amigos',
      name: 'friends',
      component: () => import('../components/Friends.vue')
    },
    {
      path: '/programas/proyecto-colegios/',
      name: 'colegios',
      component: () => import('../components/Colleges.vue')
    },
    {
      path: '/programas/talleres-de-aprendizaje',
      name: 'learning',
      component: () => import('../components/Learning.vue')
    },
    {
      path: '/programas/plan-padrino',
      name: 'father',
      component: () => import('../components/Father.vue')
    },
    {
      path: '/programas/familias',
      name: 'father',
      component: () => import('../components/Families.vue')
    },
    {
      path: '/documentos-legales',
      name: 'dian',
      component: () => import('../components/Dian.vue')
    },
    {
      path: '/contactanos',
      name: 'contactanos',
      component: () => import('../components/Contact.vue')
    }
    
  ]
})
