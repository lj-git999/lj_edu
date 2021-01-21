import Vue from 'vue'
import Router from 'vue-router'
import Course from "../components/Course";
import Index from "../components/Index";


Vue.use(Router)

export default new Router({
  routes: [
      {path:"/index",component:Index},
      {path:"/course",component:Course},
  ]
})
