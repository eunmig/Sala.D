<template>
<div> test</div>
<div>
{{ userData.id }}
</div>
</template>
  
<script setup>


import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const userData = authStore.userData
console.log(userData.id)
  </script>
  
  <style scoped>

  </style>
  