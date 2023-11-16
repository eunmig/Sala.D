import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogInView
    }
    // {
    //   path: '/posts',
    //   name: 'Post',
    //   component: PostListView
    // },
    // {
    //   path: '/post/:id',
    //   name: 'DetailView',
    //   component: DetailView
    // },
    // {
    //   path: '/createPost',
    //   name: 'CreatePost',
    //   component: CreatePostView
    // },

  ]
})

export default router
