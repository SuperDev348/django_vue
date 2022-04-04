import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../contains/home.vue';
import Detail from '../contains/detail.vue';

Vue.use(VueRouter)


export default new VueRouter({
    mode: 'history',
    routes: [
      { path: '/', component: Home},
      {path: '/todo/:id/', component: Detail}
    ]
  })