import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import AdminPage from "../components/AdminPage";
import AllTour from "../components/AllTour";
import HotTour from "../components/HotTour";
import PersonalArea from "../components/PersonalArea";


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/admin',
      name: 'adminPage',
      component: AdminPage
    },
    {
      path: '/tour',
      name: 'allTour',
      component: AllTour
    },
    {
      path: '/hot',
      name: 'hotTour',
      component: HotTour
    },
    {
      path: '/lk',
      name: 'personalArea',
      component: PersonalArea
    },
  ]
})
