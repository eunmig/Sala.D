<template>
<div> test</div>
<div>

</div>
</template>
  
<script setup>


import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const userData = authStore.userData
console.log(userData)
  </script>
  
  <style scoped>

  </style>
  