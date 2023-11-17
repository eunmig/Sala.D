<template>
    <div>
        <h2>{{ item.fin_prdt_nm }}</h2>
        <p>은행: {{ item.kor_co_nm }}</p>
        
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useFinanceStore } from '../stores/finance'
import { useAuthStore } from '../stores/auth'
import router from '../router'

const authStore = useAuthStore()
const token = authStore.token
const financeStore = useFinanceStore()
const route = useRoute()
const itemOption = ref([])
const item = ref(null)

console.log(itemOption)
console.log('item', item)

onMounted(() => {
  axios({
    method: 'get',
    url: `${financeStore.API_URL}/finance/deposit-product-options/${route.params.id}/`,
    headers: {
      Authorization: `Token ${token}`
    }
  })
  .then((res) => {
    itemOption.value = res.data
    console.log('detail res', res.data)
  })
  .catch(err => {
    console.log(err)
  })

  axios({
    method: 'get',
    url: `${financeStore.API_URL}/finance/deposit-product/${route.params.id}/`,
    headers: {
      Authorization: `Token ${token}`
    }
  })
  .then((res) => {
    item.value = res.data
    console.log('detail res', res.data)
  })
  .catch(err => {
    console.log(err)
  })
})
</script>

<style scoped>

</style>