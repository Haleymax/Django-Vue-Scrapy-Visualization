<template>
    <div ref="chartContainer" class="chart-container">
    </div>
</template>

<script setup lang="ts" name="EchartsComponent">
import { onMounted, ref } from 'vue';
import * as echarts from 'echarts';

const chartContainer = ref<HTMLDivElement>();

const initChart = () => {
    if (chartContainer.value) {
        const chart = echarts.init(chartContainer.value);
        const option = {
            title: {
                text: '示例图表'
            },
            tooltip: {},
            xAxis: {
                data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
            },
            yAxis: {},
            series: [
                {
                    name: '销量',
                    type: 'bar',
                    data: [5, 20, 36, 10, 10, 20, 40]
                }
            ]
        };
        chart.setOption(option);
    }
};

onMounted(() => {
    initChart();
});
</script>

<style scoped>
.chart-container {
    width: 100%;
    height: 400px;
}
</style>