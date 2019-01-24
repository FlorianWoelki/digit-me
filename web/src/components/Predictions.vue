<script>
import { Bar } from 'vue-chartjs';

export default {
  extends: Bar,
  mounted() {
    this.renderChart(
      {
        labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        datasets: [
          {
            label: 'Prediction',
            backgroundColor: '#f87979',
            data: [100, 0, 0, 0, 0, 0, 0]
          }
        ]
      },
      {
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
    );
  }
};
</script>
