<template>
    <div>
        <h1>왜 안나와 씨발</h1>
        <h1>{{ carInfo?.car_name }}</h1>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRoute } from 'vue-router'

const authStore = useAuthStore()
const route = useRoute()

const carInfo = ref([])

const oneCar = function() {
    axios({
        method: 'get',
        url: `${authStore.API_URL}/account/car/${route.params.car_pk}`,
        headers: {
            Authorization: `Token ${authStore.token}`
        }
    })
    .then((res) => {
        carInfo.value = res.data
    })
    .catch(err => console.log(err))
}

onMounted(() => {
    oneCar()
})
</script>

<style scoped>

</style>