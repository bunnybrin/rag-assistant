import {computed, ref, onMounted, onUnmounted} from 'vue'

export const useUrlTabs = (options) => {
  const {tabs, defaultTab, paramName = 'tab'} = options

  const tabsList = computed(() => {
    return Array.isArray(tabs) ? tabs : tabs.value
  })

  const getUrlParam = () => {
    const urlParams = new URLSearchParams(window.location.search)
    return urlParams.get(paramName)
  }

  const currentUrlTab = ref(getUrlParam())

  const activeTab = computed(() => {
    const urlTab = currentUrlTab.value
    return tabsList.value.includes(urlTab) ? urlTab : defaultTab
  })

  const setActiveTab = (tab) => {
    if (!tabsList.value.includes(tab)) return

    const url = new URL(window.location)

    if (tab === defaultTab) {
      url.searchParams.delete(paramName)
    } else {
      url.searchParams.set(paramName, tab)
    }

    window.history.pushState({}, '', url)
    currentUrlTab.value = getUrlParam()
  }

  const handlePopState = () => {
    currentUrlTab.value = getUrlParam()
  }

  onMounted(() => {
    window.addEventListener('popstate', handlePopState)
  })

  onUnmounted(() => {
    window.removeEventListener('popstate', handlePopState)
  })

  const availableTabs = computed(() => tabsList.value)

  return {
    activeTab,
    setActiveTab,
    availableTabs,
  }
}
