import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../contains/home.vue';
import Detail from '../contains/detail.vue';

Vue.use(VueRouter)

// const requireAuth = (to, from, next) => {
//   if (Auth.loggedIn()) return next()
//   next({
//     path: '/login',
//     query: { redirect: to.fullPath }
//   })
// }

export default new VueRouter({
    mode: 'history',
    routes: [
      { path: '/', component: Home},
      {path: '/todo/:id/', component: Detail}
    ]
  })