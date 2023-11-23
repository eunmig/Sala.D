<template>
    <div>
        <div v-if="showMyCar">
          <button @click="toggleMyCar">전체 차량 보기</button>
            <div v-for="car in myCar">
            <p>차량 이름: {{ car.car_name }}</p>
            <p>금액대: {{ car.price }}만원</p>
            <p>출시 연도: {{ car.year }}</p>
            <hr>
            </div>
        </div>
        <div v-else>
          <button @click="toggleMyCar">추천 받기</button>
            <div v-for="car in allCar">
            <p>차량 이름: {{ car.car_name }}</p>
            <p>금액대: {{ car.price }}만원</p>
            <p>출시 연도: {{ car.year }}</p>
            <hr>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import axios from 'axios'
import router from '../router'

const authStore = useAuthStore()
const user = authStore.userData
const myCar = ref([])
const showMyCar = ref(false)

const toggleMyCar = () => {
    showMyCar.value = !showMyCar.value
    getmyCar()
    console.log(showMyCar)
}

const getmyCar = function () {
    axios({
      method: 'get',
      url: `${authStore.API_URL}/account/my_cars/${user.salary_level}/`
    }).then((res) => {
      myCar.value = res.data
  })
}


const allCar = ref([])
onMounted(() => {
  axios({
    method: 'get',
    url: `${authStore.API_URL}/account/cars/`,
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  })
    .then((res) => {
    allCar.value = res.data
  })
    .catch(err => console.log(err))
  }
)

</script>

<style scoped>

</style>