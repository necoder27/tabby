<template>
  <div class="weather-component-container">
    <p id="weather-code-text">{{ weather?.weather_code_text }}</p>
    <p id="current-temperature">{{ weather?.current_temperature[0] }}{{ weather?.current_temperature[1] }}</p>
    <div :class="[(['uv_index_max', 'sunrise'].includes(name)) ? 'weather-list-items weather-list-items-separate' : 'weather-list-items']" v-for="[name, value] in filtered_weather" :key="name">
      <p class="weather-list-item-names">{{ name }}:</p>
      <div class="weather-list-item-values">
        <p>{{ Array.isArray(value) ? value[0] : value }}</p>
        <p>{{ Array.isArray(value) ? value[1] : "" }}</p>
      </div>
    </div>
    <p id="location">{{ location }}</p>
  </div>
</template>

<script setup lang="ts">
  import {ref, onMounted, computed} from "vue";
  import apiClient from "@/api";

  interface WeatherResponse {
    weather_code_text: string,
    current_temperature: [number, string],
    apparent_temp: [number, string],
    wind_speed_10m: [number, string],
    precipitation_probability: [number, string],
    precipitation: [number, string],
    uv_index_max: number,
    sunrise: [string, string],
    sunset: [string, string]
  }

  const weather = ref<WeatherResponse>();
  const filtered_weather = ref<[string, any][]>([]);
  const location = ref<string>("");

  async function getWeather() {
    const response = await apiClient.get("/weather");
    weather.value = response.data;
    getFilteredWeather();
  }

  function getFilteredWeather() {
    if (weather.value) {
      filtered_weather.value = Object.entries(weather.value).slice(2);
    }
  }

  async function getLocation() {
    const response = await apiClient.get("/location");
    location.value = response.data;
  }

  onMounted(async () => {
    await getWeather();
    await getLocation();
  })
</script>

<style scoped>
  .weather-component-container {
    background-color: rgba(106, 106, 106, 0.5);
    backdrop-filter: blur(5px) grayscale(100%);
    border-radius: 25px;
    display: flex;
    flex-direction: column;
    padding: 2vh 2vw;
    margin: 4vh 2vw;
    align-items: center;
    width: 20vw;
    height: fit-content;
    font-size: 2vh;
  }

  #weather-code-text {
    margin: 0;
    font-weight: 300;
    font-size: x-large;
  }

  #current-temperature {
    margin: 2vh 0;
    font-size: 5vh;
  }

  .weather-list-items {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 0;
    width: 100%;
    height: fit-content;

    p {
      margin: 0;
    }
  }

  .weather-list-items-separate {
    padding-top: 5vh;
  }

  .weather-list-item-names {
    font-weight: 300;
  }

  .weather-list-item-values {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 5vw;

    p {
      font-weight: 100;
    }
  }

  #location {
    margin: 0;
    text-align: end;
    width: 100%;
    font-weight: 300;
    font-size: x-large;
  }
</style>

