import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AudioDetailView from '../views/AudioDetail.vue'
import AudioUpdateView from '../views/AudioUpdate.vue'

const routes = [
  
  {
    path: '/api',
    name: 'home',
    component: HomeView
  },
   {
    path: '/api/:id/',
    name: 'audiodetail',
    component: AudioDetailView
  },
  {
    path: '/api/:id/edit',
    name: 'audioupdate',
    component: AudioUpdateView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
