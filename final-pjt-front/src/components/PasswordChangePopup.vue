<!-- PasswordChangePopup.vue -->
<template>
    <h1>hi</h1>
    <div>
      <div class="popup-content">
        <!-- <span class="close" @click="closePopup">&times;</span> -->
        <h2>Change Password</h2>
        <form @submit.prevent="changePassword">
          <label for="new_password1">New Password:</label>
          <input v-model="newPassword1" type="password" id="new_password1" name="new_password1" required>
  
          <label for="new_password2">Confirm Password:</label>
          <input v-model="newPassword2" type="password" id="new_password2" name="new_password2" required>
  
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useAuthStore } from '../stores/auth'
  
  const newPassword1 = ref('')
  const newPassword2 = ref('')

  const authStore = useAuthStore()

  const changePassword = function() {
    console.log('비번', newPassword1.value)
    console.log('토큰', authStore.token)
        const payload = {
            new_password1: newPassword1.value,
            new_password2: newPassword2.value
        }
        authStore.changePW(payload)
    }
  </script>
  
  <style scoped>
  
  </style>
  