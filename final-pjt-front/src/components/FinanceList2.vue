<template>
    <div>
      <div class="bankSelect">
        <label for="bankSelect">은행: </label>
        <select id="bankSelect" v-model="selectedBank" class="pl">
          <option value="">-- 선택 안함 --</option>
          <option v-for="bank in uniqueBanks" :key="bank" :value="bank">
            {{ bank }}
          </option>
        </select>
      </div>
      
    <table>
      <colgroup>
        <col style="width: 250px;">
        <col style="width: 400px;">
        <col style="width: 150px;">
        <col style="width: 350px;">
      </colgroup>
      <thead>
        <tr>
          <th>은행</th>
          <th>상품명</th>
          <th>공시 일자</th>
          <th>저축금리 / 저축 기간</th>
        </tr>
      </thead>
  
    </table>
      <FinanceListItem2
      v-for="saving in filteredProducts"
      :key="saving.fin_prdt_cd"
      :saving="saving"
      />
    </div>
  </template>
    
  <script setup>
  import FinanceListItem2 from './FinanceListItem.vue'
  import { useFinanceStore } from '@/stores/finance'
  import { computed, ref } from 'vue'
  
  const store = useFinanceStore()
  
  // Computed property to get unique bank names from products
  const uniqueBanks = computed(() => {
    const banks = new Set()
    store.savings.forEach((saving) => {
      banks.add(saving.kor_co_nm)
    })
    return Array.from(banks)
  })
  
  // Reactive variable to store the selected bank for filtering
  const selectedBank = ref('')
  
  // Computed property to filter products based on the selected bank
  const filteredProducts = computed(() => {
    if (!selectedBank.value) {
      return store.savings
    }
    return store.savings.filter((saving) => saving.kor_co_nm === selectedBank.value)
  })
  </script>
  
  <style>
  @import "@/components/FinanceList.scss"
  
  </style>
    