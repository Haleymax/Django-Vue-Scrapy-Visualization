<template>
    <div ref="chartContainer" class="chart-container"></div>
    <div ref="CategoryDate" class="chart-container"></div>
    <div ref="CountryData" class="chart-container"></div>
</template>

<script setup lang="ts" name="EchartsComponent">
import { onMounted, ref } from 'vue';
import * as echarts from 'echarts';

const chartContainer = ref<HTMLDivElement>();
const CategoryDate = ref<HTMLDivElement>();
const CountryData = ref<HTMLDivElement>();

const initChart = () => {
    if (chartContainer.value) {
        const chart = echarts.init(chartContainer.value);
        const option = {
            title: {
                text: '2024年16家跨境电商上市公司总市值数据对比'
            },
            tooltip: {},
            xAxis: {
                data: ['安克创新', '秦淮时代', '三态股份', '致酚科技', '易点天下', '华凯易语', '跨境通', '联络互动', '搭健云仓', '力盟科技', '华鼎股份', '星微股份', '子不语', '乐舱物流', '有棵树', '兰亭集势', '泛远国际']
            },
            yAxis: {},
            series: [
                {
                    name: '市值数据',
                    type: 'bar',
                    data: [360.09, 121.19, 117.54, 96.04, 93.29, 71.63, 58.27, 56.82, 53.7, 39.08, 37.87, 28.33, 25.03, 14.01, 11.82, 8.71, 6.96]
                }
            ]
        };
        chart.setOption(option);
    }

    if (CategoryDate.value) {
        const chart = echarts.init(CategoryDate.value);
        const option = {
            title: {
                text: '2024年中国跨境电商商品占比百分图'
            },
            tooltip: {},
            series: [
                {
                    name: '商品占比',
                    type: 'pie',
                    data: [
                        { value: 40, name: '电子产品' },
                        { value: 20, name: '服装' },
                        { value: 20, name: '家居用品' },
                        { value: 10, name: '玩具' },
                        { value: 10, name: '其他' }
                    ]
                }
            ]
        };
        chart.setOption(option);

        if (CountryData.value) {
            const chart = echarts.init(CountryData.value);
            const option = {
            title: {
                text: '2024年中国跨境电商主要出口国家数据对比'
            },
            tooltip: {},
            series: [
                {
                    name: '国家占比',
                    type: 'pie',
                    data: [
                        { value: 600, name: '美国' },
                        { value: 450, name: '欧洲' },
                        { value: 300, name: '东南亚' },
                        { value: 150, name: '日本' },
                        { value: 100, name: '韩国' },
                        { value: 80, name: '澳大利亚' },
                        { value: 120, name: '其他' }
                    ]
                }
            ]
        };
        chart.setOption(option);
        }
    }
};

onMounted(() => {
    initChart();
});
</script>

<style scoped>
.chart-container {
    width: 500px;
    height: 500px;
}
</style>