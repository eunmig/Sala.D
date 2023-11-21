<template>
  <div>
    <div class="table-container">
      <table>
        <colgroup>
          <col style="width: 300px;">
          <col style="width: 600px;">
          <col style="width: 150px;">
        </colgroup>
        <tbody>
          <tr>
            <td>{{ product.kor_co_nm }}</td>
            <td>
              <RouterLink :to="{ name: 'FinanceItemDetail', params: { id: product.fin_prdt_cd } }">
                {{ product.fin_prdt_nm }}
              </RouterLink>
            </td>
            <td>{{ product.dcls_strt_day }}</td>
            <td v-for="option in product.depositoptions_set">{{ option.intr_rate }} / {{ option.save_trm }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
defineProps({ product: Object });
</script>

<style>
@import "@/components/FinanceListItem.scss"

</style>
