<!-- <template>
  <div>
    <h1>Currency Converter</h1>
    <div v-if="currencies.length">
      <label for="fromCurrency">From Currency:</label>
      <select v-model="fromCurrency" id="fromCurrency">
        <option v-for="currency in currencies" :key="currency.id" :value="currency.id">
          {{ currency.currency_name }}
        </option>
      </select>

      <label for="toCurrency">To Currency:</label>
      <select v-model="toCurrency" id="toCurrency">
        <option v-for="currency in currencies" :key="currency.id" :value="currency.id">
          {{ currency.currency_name }}
        </option>
      </select>

      <label for="amount">Amount:</label>
      <input v-model="amount" type="number" id="amount" />

      <p>{{ convertCurrency() }}</p>
    </div>
  </div>
</template>

<script>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useCommunityStore } from '@/stores/community'

  const store = useCommunityStore()
  

  export default {
  setup() {
  const currencies = ref([])
  const fromCurrency = ref(null)
  const toCurrency = ref(null)
  const amount = ref(1)

  const fetchCurrencies = () => {

    axios.get(`${store.API_URL}/exchange/get/`)
      .then(response => {
        currencies.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching currencies:', error);
      })
  }
  
  const convertCurrency = () => {
    if (fromCurrency.value && toCurrency.value) {
      const fromRate = currencies.value.find(c => c.id === fromCurrency.value).rate
      const toRate = currencies.value.find(c => c.id === toCurrency.value).rate
      const result = (amount.value / fromRate) * toRate
      return `${amount.value} ${currencies.value.find(c => c.id === fromCurrency.value).currency_name} = ${result.toFixed(4)} ${currencies.value.find(c => c.id === toCurrency.value).currency_name}`
    }
    return ''
  }

  onMounted(() => {
    fetchCurrencies()
  })

  return {
    currencies,
    fromCurrency,
    toCurrency,
    amount,
    fetchCurrencies,
    convertCurrency,
  }
},
}
</script>

<style scoped>

</style> -->
