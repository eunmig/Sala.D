<template>
    <div class="two alt-two">
        <h1>금융 아이템 목록 페이지
            <span>예적금 목록</span>
        </h1>
        <br>
    </div>
    <div v-if="switchItems">
    <FinanceList2/>
    </div>
    <div v-else>
    <FinanceList/>
    </div>  
    <br>
</template>

<script setup>
import FinanceList from '../components/FinanceList.vue'
import FinanceList2 from '../components/FinanceList2.vue'
import { onMounted } from 'vue'
import { useFinanceStore } from '../stores/finance'

const store = useFinanceStore()

const toggleSwitch = () {
    switchItems.value = !switchItems.value
}
const switchItems = ref(false)

onMounted(()=> {
    store.getProducts()
    store.getSavingsProducts()
    console.log('onMount: FinancialListView.vue')
})
</script>

<style scoped>
@import "@/views/FinanceListView.scss"

</style>