<template>
  <div class="two alt-two">
    <h1>{{ item?.fin_prdt_nm }}
        <span>{{ item?.kor_co_nm }}</span>
    </h1>
    <br>
  </div>
  <button class="btn btn-primary disabled" @click="toggleLike">
    {{ isLiked ? '관심 상품 해제' : '관심 상품 등록' }}
  </button>
  <div>
    <table>
      <thead>
        <tr>
          <th>상품명</th>
          <th>은행명</th>
          <th>상품 설명</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ item?.fin_prdt_nm }}</td>
          <td>{{ item?.kor_co_nm }}</td>
          <td v-html="formattedEtcNote"></td>
        </tr>
        <br>
        <tr>
          <td colspan="3">
            <!-- 추가된 행에 OptionList 컴포넌트 추가 -->
            <OptionList :options="itemOption" />
          </td>
        </tr>
      </tbody>
    </table>
    <br>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useFinanceStore } from '../stores/finance';
import { useAuthStore } from '../stores/auth';
import OptionList from '../components/OptionList.vue';

const authStore = useAuthStore();
const token = authStore.token;
const financeStore = useFinanceStore();
const route = useRoute();
const itemOption = ref([]);
const item = ref(null);
const isLiked = ref(false);

const formattedEtcNote = computed(() => {
  return item.value?.etc_note ? item.value.etc_note.replace(/\n/g, '<br>') : '';
});

const fetchData = async () => {
  try {
    const optionsResponse = await axios.get(`${financeStore.API_URL}/finance/deposit-product-options/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    itemOption.value = optionsResponse.data;
    console.log('상품 옵션 res', optionsResponse.data);

    const productResponse = await axios.get(`${financeStore.API_URL}/finance/deposit-product/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    item.value = productResponse.data;
    console.log('금융상품 res', productResponse.data);

    // Check if the current user has liked the product
    isLiked.value = productResponse.data.like_users.includes(authStore.userData.id);
  } catch (error) {
    console.error(error);
  }
}

const toggleLike = async () => {
  try {
    const likeResponse = await axios.post(
      `${financeStore.API_URL}/finance/likes/${item.value.fin_prdt_cd}/`,
      { product_cd: item.value.fin_prdt_cd }, // Include fin_prdt_cd in the request body
      {
        headers: {
          Authorization: `Token ${token}`
        }
      }
    );
    
    // Update isLiked based on the server response
    isLiked.value = likeResponse.data.liked;
  } catch (error) {
    console.error('Error toggling like:', error);
  }
}

onMounted(() => {
  fetchData();
  console.log('onMount: FinanceDetailView');
});
</script>

<style scoped>
@import "@/views/FinanceDetailView.scss"
/* Add your component-specific styles here if needed */
</style>
