<template>
<h3>{{ userData.username }}</h3>
<div>
  <p>이름: {{ userData.last_name }}{{ userData.first_name }}</p>
  <p>이메일: {{ userData.email }}</p>
  <p>연봉: {{ userData.salary }}</p>
  <PasswordChangePopup />
</div>
</template>
  
<script setup>
import PasswordChangePopup from '../components/PasswordChangePopup.vue'
import { useAuthStore } from '../stores/auth'
import { ref } from 'vue'
const authStore = useAuthStore()
const userData = authStore.userData
  </script>
  
  <style scoped>

  </style>
  