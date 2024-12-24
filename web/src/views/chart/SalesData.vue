<template>
    <div ref="" style="width: 600px; height: 400px;">

    </div>
</template>

<script setup lang="ts" name="SalesChart">
import { ref, onMounted, onUnmounted, nextTick } from 'vue';
import * as echarts from 'echarts';

const chartDom = ref(null);
let chartInstance = null;

onMounted(async () => {
    await nextTick();
    chartInstance = echarts.init(chartDom.value);
    const option = {
        title: {
            text: 'ECharts 示例图'
        },
        tooltip: {},
        
    }
})

</script>