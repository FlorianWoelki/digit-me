<script>
import { Bar, mixins } from 'vue-chartjs';
const { reactiveProp } = mixins;

export default {
  extends: Bar,
  mixins: [reactiveProp],
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        scales: {
          xAxes: [
            {
              gridLines: {
                display: false
              }
            }
          ],
          yAxes: [
            {
              gridLines: {
                display: false
              }
            }
          ]
        }
      }
    };
  },
  mounted() {
    this.renderChart(this.chartData, this.chartOptions);
  }
};
</script>
