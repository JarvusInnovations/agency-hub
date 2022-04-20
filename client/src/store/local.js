import { reactive } from 'vue'
import ls from 'local-storage-json'

const LS_KEY = 'GLOBAL_STORE'

export default ({ app }) => {
  const state = reactive(ls.get(LS_KEY) || {})
  const update = (data) => {
    Object.assign(state, data)
    ls.set(LS_KEY, state)
  }
  const getActiveAgency = () => {
    const { user } = app.config.globalProperties.$auth
    if (!user) {
      return null
    }
    const { selected_agency_id } = state
    const { agencies } = user
    return agencies.find(a => a.id === selected_agency_id) || agencies[0]
  }

  const setActiveAgency = (agency) => update({ selected_agency_id: agency.id })

  const getActiveDashboard = () => {
    const dashboards = app.config.globalProperties.$store.dashboard.getAll()
    if (!dashboards) {
      return null
    }
    const { selected_dashboard_id } = state
    return dashboards.find(d => d.id === selected_dashboard_id) || dashboards[0]
  }

  const setActiveDashboard = (dashboard) => update({ selected_dashboard_id: dashboard.id })

  return {
    update,
    getActiveAgency,
    setActiveAgency,
    getActiveDashboard,
    setActiveDashboard,
  }
}