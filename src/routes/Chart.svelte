<!-- src/Chart.svelte -->
<script>
  import { onDestroy, onMount } from 'svelte';
  // import { Chart } from 'chart.js/auto'

  let chart; // Chart.js instance

  // Data for the chart
  const data = {
    labels: ['January', 'February', 'March', 'April', 'May'],
    datasets: [
      {
        label: 'Sample Data',
        data: [65, 59, 67, 81, 56],
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 2,
      },
    ],
  };

  const config = {
    type: 'line', // Change the chart type as needed (e.g., 'bar', 'pie', 'radar', etc.)
    data: data,
  };

  onMount(() => {
    // Create a new Chart.js instance when the component mounts
    // const ctx = document.getElementById('myChart').getContext('2d');
    // console.log(ctx);
    // console.log('blub');
    // chart = new Chart(ctx, config);
  });
  onDestroy(() => {
//     if(chart && chart.ctx) {
//       chart.ctx
// ;    };
  })
</script>

<style>
  /* Add any custom styles for the chart container */
  .chart-container {
    max-width: 600px;
    margin: 0 auto;
  }
</style>

<div class="chart-container">
  <canvas width="600px" height="" id="myChart"></canvas>
</div>
