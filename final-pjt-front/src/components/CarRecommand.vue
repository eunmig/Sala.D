<template>
    <div>
        Car
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const data = authStore.userData
console.log('car', userData)

onMounted(() => {
    authStore.getCar()
    console.log(authStore.allCar)
})
</script>

<style scoped>

</style>