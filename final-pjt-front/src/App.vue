<template>
  <div>
    <div class="login-status">
      로그인 상태
    </div>
    <nav>
      <RouterLink class="link" :to="{ name:'Home' }">Home</RouterLink> | 
      
    </nav>
    <h1>시작</h1>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>