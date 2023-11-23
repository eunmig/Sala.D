<template>
    <div>
        <div v-if="carInfo">
            <h1>{{ carInfo.car_name }}</h1>
            <img :src="imageroute" alt="아직 준비되지 않았습니다">
            <p>{{ carInfo.price }}만원</p>
            <p>출시 연도: {{ carInfo.year }}</p>
            <p>나의 연봉: {{ user.salary }}</p>
        </div>
        <div v-else>
            <p>Loading...</p>
        </div>
    </div>

      <h2>추천 상품</h2>
      <table>
        <thead>
          <tr>
            <th>은행명</th>
            <th>상품이름</th>
            <th>최고 우대 금리</th>
            <th>기간</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(recommendation, index) in bestProduct.recommendations" :key="index">
            <td>{{ recommendation.deposit_product.kor_co_nm }}</td>
            <td>              
                <RouterLink :to="{ name: 'FinanceItemDetail', params: { id: recommendation.deposit_product.fin_prdt_cd } }">
                {{ recommendation.deposit_product.fin_prdt_nm }}
                 </RouterLink>
            </td>
            <td>{{ recommendation.options.intr_rate }}%</td>
            <td>{{ recommendation.options.save_trm }} 개월</td>
          </tr>
        </tbody>
      </table>

</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRoute } from 'vue-router'
import { RouterLink } from 'vue-router'

const authStore = useAuthStore()
const user = authStore.userData
const route = useRoute()

const carInfo = ref([])
const imageroute = computed(() => `../src/assets/${carInfo.value.car_name}.png`)

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

const bestProduct = ref([])
const recProducts = function() {
    axios({
        method: 'get',
        url: `${authStore.API_URL}/finance/deposit-products/top_rate/`,
        headers: {
            Authorization: `Token ${authStore.token}`
        }
    })
    .then((res) => {
        bestProduct.value = res.data
    })
    .catch(err => console.log(err))
}

onMounted(() => {
    oneCar()
    recProducts()
})
</script>

<style scoped>

</style>