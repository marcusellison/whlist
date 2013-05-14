

$(document).ready(function() {
  mixpanel.track("Page Views", { Target:"Technology"});
  mixpanel.track_forms("#view_jobs", "Job List Requests", { Location: "NYC"});
  mixpanel.track_links(".job_url", "Job Clicks", { Type:"Technology"});
});