<template>
 <h1>차량 추천</h1>
 <CarList/>

</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import CarList from '../components/CarList.vue'

const authStore = useAuthStore()

onMounted(() => {
  authStore.getCar()
})


</script>

<style scoped>

</style>