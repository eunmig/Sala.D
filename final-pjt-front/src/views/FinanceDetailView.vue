<template>

</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useFinanceStore } from '../stores/finance'
import { useAuthStore } from '../stores/auth'
import router from '../router'
import OptionList from '../components/OptionList.vue'


const authStore = useAuthStore()
const token = authStore.token
const financeStore = useFinanceStore()
const route = useRoute()
const itemOption = ref([])
const item = ref(null)
const id = route.params.id

console.log(id)
console.log('option',itemOption)
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
    console.log('상품 옵션 res', res.data)
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
    console.log('금융상품 res', res.data)
  })
  .catch(err => {
    console.log(err)
  })
})

</script>

<style scoped>

</style>