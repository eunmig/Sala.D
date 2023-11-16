import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
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
    //   path: '/createCategory',
    //   name: 'CreateCategory',
    //   component: CreateCategoryView
    // },
    // {
    //   path: '/createPost',
    //   name: 'CreatePost',
    //   component: CreatePostView
    // },
    // {
    //   path: '/signup',
    //   name: 'SignUp',
    //   component: SignUpView
    // },
    // {
    //   path: '/login',
    //   name: 'LogInView',
    //   component: LogInView
    // }
  ]
})

export default router
