// Supabase publishable keys are safe for browser use. Row Level Security
// protects private Eden data; never place a Supabase service-role key here.
window.EDEN_SUPABASE_URL = 'https://ppzdymxnpjuwhdzchafn.supabase.co';
window.EDEN_SUPABASE_PUBLISHABLE_KEY = 'sb_publishable_QHZKh4wrSIvTcSPhWm_0LQ_KGh0Lh6v';

// Billing sessions are created server-side by Supabase Edge Functions. Never
// place a Stripe secret key in this browser file.
window.EDEN_BILLING_FUNCTION_BASE =
  `${window.EDEN_SUPABASE_URL}/functions/v1`;

// This is the deployed Eden application, not a local-development address.
window.EDEN_APP_URL = 'https://edenconintel-preview.streamlit.app/';

// The app's root route shows the Eden sign-in screen.
window.EDEN_APP_LOGIN_URL = window.EDEN_APP_URL;
