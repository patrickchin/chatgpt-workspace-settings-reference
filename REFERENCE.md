# Observed key reference

One response observed on 2026-11-19; no observed values are published. See [scope and evidence rules](README.md).

`[]` represents observed array item shapes. `*` replaces every identifier in reviewed role maps, including built-in role keys. Multiple identifiers and repeated items collapse to distinct path/type pairs. Null and empty collections establish no hidden schema types.

Official links provide product context, not confirmation of an internal JSON key. All backend mappings below remain inferred or unknown except the explicitly attributed Windows client observation supplied by the source author.

## Contents

- [access_request](#access_request)
- [access_token_max_ttl](#access_token_max_ttl)
- [admin_preview_launch_defaults](#admin_preview_launch_defaults)
- [admin_preview_launch_settings](#admin_preview_launch_settings)
- [admin_preview_matching](#admin_preview_matching)
- [admin_work_local_enabled](#admin_work_local_enabled)
- [admin_work_mode_enabled](#admin_work_mode_enabled)
- [allow_external_domain_invites](#allow_external_domain_invites)
- [allow_third_party_gpts](#allow_third_party_gpts)
- [allowed_custom_actions_domains](#allowed_custom_actions_domains)
- [allowed_web_search_domains](#allowed_web_search_domains)
- [auto_accept_requests](#auto_accept_requests)
- [auto_approve_seat_upgrades](#auto_approve_seat_upgrades)
- [auto_join_pending_requests_enabled](#auto_join_pending_requests_enabled)
- [available_admin_preview_features](#available_admin_preview_features)
- [beta_settings](#beta_settings)
- [beta_settings_dict](#beta_settings_dict)
- [beta_settings_str](#beta_settings_str)
- [composer_predictions_launched](#composer_predictions_launched)
- [conversation_ttl](#conversation_ttl)
- [custom_permission_inheritance_enabled](#custom_permission_inheritance_enabled)
- [default_seat_type](#default_seat_type)
- [desktop_app_beta_policy](#desktop_app_beta_policy)
- [disable_account_switching](#disable_account_switching)
- [enable_account_switching](#enable_account_switching)
- [file_library_auto_reference_admin_control_retired](#file_library_auto_reference_admin_control_retired)
- [library_sharing_control_mode](#library_sharing_control_mode)
- [member_profile_activity_enabled](#member_profile_activity_enabled)
- [member_profiles_enabled](#member_profiles_enabled)
- [member_profiles_sharing](#member_profiles_sharing)
- [model_permission_preferences](#model_permission_preferences)
- [orbit_rollout_eligible](#orbit_rollout_eligible)
- [orbit_uses_workspace_setting](#orbit_uses_workspace_setting)
- [owner_setup_join_preference_confirmed](#owner_setup_join_preference_confirmed)
- [permissions](#permissions)
- [plugin_incentive_campaigns](#plugin_incentive_campaigns)
- [plugin_incentives_ui_enabled](#plugin_incentives_ui_enabled)
- [public_display_name](#public_display_name)
- [role_summaries](#role_summaries)
- [search_restrictions](#search_restrictions)
- [seat_type_credit_limits](#seat_type_credit_limits)
- [settings](#settings)
- [share_settings](#share_settings)
- [support_workspace_discovery](#support_workspace_discovery)
- [unified_workspace_name](#unified_workspace_name)
- [usage_limit_increase_request](#usage_limit_increase_request)
- [use_workspace_name_for_discovery](#use_workspace_name_for_discovery)
- [workspace_banner_available](#workspace_banner_available)
- [workspace_discoverable](#workspace_discoverable)
- [workspace_id](#workspace_id)
- [workspace_referrals_enabled](#workspace_referrals_enabled)
- [workspace_referrals_enabled_visible](#workspace_referrals_enabled_visible)

## access_request

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["access_request"]` | `null` | Access-request information or configuration; the observed null does not reveal its structure. | Inferred from name | No supporting public source located. |

## access_token_max_ttl

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["access_token_max_ttl"]` | `integer` | Maximum lifetime of an access token. Units, token class, and enforcement are not verified; do not assume seconds. | Inferred from name | No supporting public source located. |

## admin_preview_launch_defaults

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["admin_preview_launch_defaults"]` | `object` | Per-feature starting states for an admin preview; these response values are not product defaults. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_defaults"]["admin_preview_gpt_6_2_astra"]` | `string` | Starting preview policy state for the preview identified as gpt_6_2_astra; this name does not establish public model availability. This is a response value, not a universal product default. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_defaults"]["admin_preview_gpt_6_2_sol"]` | `string` | Starting preview policy state for the preview identified as gpt_6_2_sol; this name does not establish public model availability. This is a response value, not a universal product default. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_defaults"]["admin_preview_library_sharing"]` | `string` | Starting preview policy state for Library sharing. This is a response value, not a universal product default. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_defaults"]["admin_preview_library_workspace_link_sharing"]` | `string` | Starting preview policy state for Library links scoped to the workspace. This is a response value, not a universal product default. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_defaults"]["admin_preview_team_automations"]` | `string` | Starting preview policy state for team automations. This is a response value, not a universal product default. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_defaults"]["admin_preview_team_create"]` | `string` | Starting preview policy state for team creation. This is a response value, not a universal product default. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |

## admin_preview_launch_settings

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["admin_preview_launch_settings"]` | `object` | Per-feature role-policy maps for an admin preview; inheritance and precedence are not verified. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_settings"]["admin_preview_gpt_6_1_terra"]` | `object` | Role-policy map for the preview identified as gpt_6_1_terra; this name does not establish public model availability. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_settings"]["admin_preview_gpt_6_1_terra"]["*"]` | `string` | Policy state under a redacted role-map key. All role identifiers, including built-in role keys, collapse to this path; assignment and policy values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_settings"]["admin_preview_library_sharing"]` | `object` | Role-policy map for Library sharing. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_settings"]["admin_preview_library_sharing"]["*"]` | `string` | Policy state under a redacted role-map key. All role identifiers, including built-in role keys, collapse to this path; assignment and policy values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_settings"]["admin_preview_team_create"]` | `object` | Role-policy map for team creation. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_launch_settings"]["admin_preview_team_create"]["*"]` | `string` | Policy state under a redacted role-map key. All role identifiers, including built-in role keys, collapse to this path; assignment and policy values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |

## admin_preview_matching

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["admin_preview_matching"]` | `object` | Per-preview synchronization or matching metadata; the source of matching and algorithm are unverified. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]` | `object` | Matching or synchronization metadata for the preview identified as gpt_6_2_astra; this name does not establish public model availability. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["can_edit_sync"]` | `boolean` | Whether editing the preview synchronization selection is allowed. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["mode"]` | `string` | Matching/synchronization strategy for this preview; the complete strategy enum is unknown. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["revision"]` | `string` | Opaque revision marker for preview-matching state; algorithm and concurrency semantics are unverified. Actual marker omitted. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["saved_sync"]` | `boolean` | Saved synchronization selection for this preview; a saved selection may differ from enforced behavior. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["show_sync_toggle"]` | `boolean` | Whether the client should show a synchronization toggle for this preview. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]` | `object` | Matching or synchronization metadata for the preview identified as gpt_6_2_sol; this name does not establish public model availability. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["can_edit_sync"]` | `boolean` | Whether editing the preview synchronization selection is allowed. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["mode"]` | `string` | Matching/synchronization strategy for this preview; the complete strategy enum is unknown. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["revision"]` | `string` | Opaque revision marker for preview-matching state; algorithm and concurrency semantics are unverified. Actual marker omitted. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["saved_sync"]` | `boolean` | Saved synchronization selection for this preview; a saved selection may differ from enforced behavior. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["show_sync_toggle"]` | `boolean` | Whether the client should show a synchronization toggle for this preview. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]` | `object` | Matching or synchronization metadata for Library sharing. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["can_edit_sync"]` | `boolean` | Whether editing the preview synchronization selection is allowed. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["mode"]` | `string` | Matching/synchronization strategy for this preview; the complete strategy enum is unknown. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["revision"]` | `string` | Opaque revision marker for preview-matching state; algorithm and concurrency semantics are unverified. Actual marker omitted. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["saved_sync"]` | `boolean` | Saved synchronization selection for this preview; a saved selection may differ from enforced behavior. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["show_sync_toggle"]` | `boolean` | Whether the client should show a synchronization toggle for this preview. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]` | `object` | Matching or synchronization metadata for Library links scoped to the workspace. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["can_edit_sync"]` | `boolean` | Whether editing the preview synchronization selection is allowed. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["mode"]` | `string` | Matching/synchronization strategy for this preview; the complete strategy enum is unknown. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["revision"]` | `string` | Opaque revision marker for preview-matching state; algorithm and concurrency semantics are unverified. Actual marker omitted. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["saved_sync"]` | `boolean` | Saved synchronization selection for this preview; a saved selection may differ from enforced behavior. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["show_sync_toggle"]` | `boolean` | Whether the client should show a synchronization toggle for this preview. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_automations"]` | `object` | Matching or synchronization metadata for team automations. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["can_edit_sync"]` | `boolean` | Whether editing the preview synchronization selection is allowed. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["mode"]` | `string` | Matching/synchronization strategy for this preview; the complete strategy enum is unknown. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["revision"]` | `string` | Opaque revision marker for preview-matching state; algorithm and concurrency semantics are unverified. Actual marker omitted. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["saved_sync"]` | `boolean` | Saved synchronization selection for this preview; a saved selection may differ from enforced behavior. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["show_sync_toggle"]` | `boolean` | Whether the client should show a synchronization toggle for this preview. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_create"]` | `object` | Matching or synchronization metadata for team creation. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["admin_preview_matching"]["admin_preview_team_create"]["can_edit_sync"]` | `boolean` | Whether editing the preview synchronization selection is allowed. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_create"]["mode"]` | `string` | Matching/synchronization strategy for this preview; the complete strategy enum is unknown. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_create"]["revision"]` | `string` | Opaque revision marker for preview-matching state; algorithm and concurrency semantics are unverified. Actual marker omitted. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_create"]["saved_sync"]` | `boolean` | Saved synchronization selection for this preview; a saved selection may differ from enforced behavior. | Inferred from name | No supporting public source located. |
| `$["admin_preview_matching"]["admin_preview_team_create"]["show_sync_toggle"]` | `boolean` | Whether the client should show a synchronization toggle for this preview. | Inferred from name | No supporting public source located. |

## admin_work_local_enabled

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["admin_work_local_enabled"]` | `boolean` | Availability of local Work functionality; do not equate this field with local Codex access without further evidence. | Inferred from name | [OpenAI Work and Codex access](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) (product context; key mapping unverified) |

## admin_work_mode_enabled

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["admin_work_mode_enabled"]` | `boolean` | Administrative gate for Work; whether it specifically gates cloud Work is unverified. | Inferred from name | [OpenAI Work and Codex access](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) (product context; key mapping unverified) |

## allow_external_domain_invites

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["allow_external_domain_invites"]` | `boolean` | Whether invitations to addresses outside workspace-associated domains are allowed. | Inferred from name | [OpenAI workspace membership and discovery](https://help.openai.com/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business) (product context; key mapping unverified) |

## allow_third_party_gpts

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["allow_third_party_gpts"]` | `string` | Policy selecting access to GPTs created outside the workspace; the complete accepted value set is unknown. | Inferred from name | [OpenAI GPT access controls](https://help.openai.com/en/articles/8555535-managing-gpt-access-in-enterprise-and-edu-workspaces) (product context; key mapping unverified) |

## allowed_custom_actions_domains

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["allowed_custom_actions_domains"]` | `null` | Domain restriction or allowlist for GPT custom actions. Null does not establish unrestricted access or list type. | Inferred from name | [OpenAI GPT access controls](https://help.openai.com/en/articles/8555535-managing-gpt-access-in-enterprise-and-edu-workspaces) (product context; key mapping unverified) |

## allowed_web_search_domains

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["allowed_web_search_domains"]` | `null` | Domain restriction or allowlist for web search. Null does not establish unrestricted access or list type. | Inferred from name | [OpenAI web search](https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt) (product context; key mapping unverified) |

## auto_accept_requests

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["auto_accept_requests"]` | `boolean` | Automatically accepting requests to join a discoverable workspace. | Inferred from name | [OpenAI workspace membership and discovery](https://help.openai.com/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business) (product context; key mapping unverified) |

## auto_approve_seat_upgrades

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["auto_approve_seat_upgrades"]` | `boolean` | Automatically approving requested seat upgrades; billing and eligibility rules remain unspecified. | Inferred from name | [OpenAI workspace membership and discovery](https://help.openai.com/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business) (product context; key mapping unverified) |

## auto_join_pending_requests_enabled

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["auto_join_pending_requests_enabled"]` | `boolean` | Automatically joining or processing members with pending requests; distinct from the auto_accept_requests field. | Inferred from name | No supporting public source located. |

## available_admin_preview_features

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["available_admin_preview_features"]` | `object` | Map of preview feature identifiers to arrays of permission identifiers associated with each preview. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_gpt_6_2_astra"]` | `array` | Permission identifiers associated with the preview identified as gpt_6_2_astra; this name does not establish public model availability. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_gpt_6_2_astra"][]` | `string` | One permission identifier associated with the preview identified as gpt_6_2_astra; this name does not establish public model availability; actual permission values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_gpt_6_2_sol"]` | `array` | Permission identifiers associated with the preview identified as gpt_6_2_sol; this name does not establish public model availability. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_gpt_6_2_sol"][]` | `string` | One permission identifier associated with the preview identified as gpt_6_2_sol; this name does not establish public model availability; actual permission values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_library_sharing"]` | `array` | Permission identifiers associated with Library sharing. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_library_sharing"][]` | `string` | One permission identifier associated with Library sharing; actual permission values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_library_workspace_link_sharing"]` | `array` | Permission identifiers associated with Library links scoped to the workspace. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_library_workspace_link_sharing"][]` | `string` | One permission identifier associated with Library links scoped to the workspace; actual permission values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_team_automations"]` | `array` | Permission identifiers associated with team automations. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_team_automations"][]` | `string` | One permission identifier associated with team automations; actual permission values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_team_create"]` | `array` | Permission identifiers associated with team creation. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["available_admin_preview_features"]["admin_preview_team_create"][]` | `string` | One permission identifier associated with team creation; actual permission values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |

## beta_settings

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["beta_settings"]` | `object` | Container of feature availability, policy, and rollout flags. The beta name does not prove that each feature is currently experimental. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["agent_mode"]` | `boolean` | Availability of ChatGPT agent mode; other restrictions may still prevent use. | Inferred from name | [OpenAI Lockdown Mode](https://help.openai.com/en/articles/20001061-lockdown-mode) (product context; key mapping unverified) |
| `$["beta_settings"]["allow_computer_history"]` | `boolean` | Permission to use a Computer History capability; it is distinct from the Windows Computer Use flag. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["app_pairing"]` | `boolean` | Pairing an app or client with another surface or device; what is paired is unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["aura"]` | `boolean` | Opaque feature identifier; no product mapping has been verified. | Unknown | No supporting public source located. |
| `$["beta_settings"]["aura_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of aura (unidentified feature); current access, rollout completion, and precedence are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["auto_scim_groups_to_teams"]` | `boolean` | Automatic mapping or conversion of SCIM-provisioned groups into teams; exact synchronization behavior is unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["basispoints_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of basispoints (unidentified feature); current access, rollout completion, and precedence are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["basispoints_powerpoint_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of the PowerPoint variant of basispoints (unidentified feature); current access, rollout completion, and precedence are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["browsing"]` | `boolean` | Access to web browsing or search; the name alone does not establish which current web-search experience it gates. | Inferred from name | [OpenAI web search](https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings"]["canvas"]` | `boolean` | Availability of Canvas, the writing and coding surface exposed through ChatGPT workspace controls. | Inferred from name | [OpenAI workspace controls](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) (product context; key mapping unverified) |
| `$["beta_settings"]["canvas_code_execution"]` | `boolean` | Running code within Canvas; distinct from merely opening or editing a Canvas. | Inferred from name | [OpenAI Canvas launch and Python execution (December 10, 2024)](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) (product context; key mapping unverified) |
| `$["beta_settings"]["canvas_code_network_access"]` | `boolean` | Allowing Canvas-generated code to make network requests; separate security restrictions can still apply. | Inferred from name | [OpenAI Lockdown Mode](https://help.openai.com/en/articles/20001061-lockdown-mode) (product context; key mapping unverified) |
| `$["beta_settings"]["client_application_apple"]` | `boolean` | Apple-client availability policy; supported platforms and enforcement points are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["client_application_apple_mdm_required"]` | `boolean` | Requirement for mobile device management (MDM) on an Apple client; this does not identify any Mac Computer Use gate. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["code_interpreter"]` | `boolean` | Access to code-backed data analysis, commonly associated with the Code Interpreter capability; exact legacy-key mapping is unverified. | Inferred from name | [OpenAI data analysis](https://help.openai.com/en/articles/8437071-advanced-data-) (product context; key mapping unverified) |
| `$["beta_settings"]["codex_admin"]` | `boolean` | Availability of Codex administrative functions; does not prove the caller holds an admin role. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_agent_network_access"]` | `boolean` | Permission for a Codex agent to access the network; scope and local sandbox interaction are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_code_attribution_analytics"]` | `boolean` | Analytics about attribution of code to Codex; collection details are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_composer_predictions"]` | `boolean` | Predicted text or suggestions in the Codex prompt composer; trigger and implementation are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_device_code_auth"]` | `boolean` | Availability of device-code authentication for Codex clients; not a credential value. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_git_attribution"]` | `boolean` | Git attribution behavior associated with Codex-generated changes; format and enforcement are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_remote_control"]` | `boolean` | Access to remote-control functionality associated with Codex; controlled surfaces are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_security"]` | `boolean` | Availability of a Codex security-related feature; exact security product mapping is unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_security_admin"]` | `boolean` | Administrative access for a Codex security-related feature; not proof of an assigned admin role. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_slack_posting"]` | `boolean` | Ability for Codex-related workflows to post in Slack; required app authorization is not established here. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["codex_usage_leaderboard"]` | `boolean` | Visibility or availability of a Codex usage leaderboard. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["context_connector_confluence"]` | `boolean` | Connector availability associated with Confluence content. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["context_connector_gdrive"]` | `boolean` | Connector availability associated with Google Drive content. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["context_connector_java"]` | `boolean` | Connector identifier containing java; the provider or feature mapping is unknown. | Unknown | No supporting public source located. |
| `$["beta_settings"]["context_connector_notion"]` | `boolean` | Connector availability associated with Notion content. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["context_connector_o365_business"]` | `boolean` | Connector availability associated with business Microsoft 365 accounts. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["context_connector_o365_personal"]` | `boolean` | Connector availability associated with personal Microsoft 365 accounts. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["context_connector_slack"]` | `boolean` | Connector availability associated with Slack content. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["dalle"]` | `boolean` | Image-generation-related flag named after DALL-E. It does not establish that the retired DALL-E GPT is available or identify the current image model. | Inferred from name | [OpenAI Images in ChatGPT](https://help.openai.com/en/articles/11084440-images-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings"]["deep_research"]` | `boolean` | Access to deep research, which researches multiple sources and produces a documented report. | Inferred from name | [OpenAI deep research](https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings"]["developer_mode"]` | `boolean` | Availability of developer-mode features; the affected developer tools and enforcement are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["enable_conversation_classifier"]` | `boolean` | Enabling an internal conversation-classification mechanism; labels, processing, and usage are unknown. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["enable_free_trial_seats"]` | `boolean` | Availability of trial seat provisioning; eligibility and billing conditions are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["enable_message_feedback"]` | `boolean` | Availability of feedback controls on messages; feedback storage or use is not established. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["enable_plugins"]` | `boolean` | Plugin enablement flag; precedence relative to the separate plugins flag is unverified. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["enable_value_survey_campaign"]` | `boolean` | Availability of a survey campaign about product value; targeting and schedule are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["enhanced_citations"]` | `boolean` | A citation presentation or generation enhancement; exact formatting behavior is unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["file_library_auto_reference"]` | `boolean` | Automatic use or referencing of files from the Library; selection rules are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["file_library_auto_reference_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of automatic Library file referencing; effective access rules are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["flora_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of flora (unidentified feature); current access, rollout completion, and precedence are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["gpt51_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of the GPT-5.1 rollout; current access, rollout completion, and precedence are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["hermes"]` | `boolean` | Opaque feature identifier; no product mapping has been verified. | Unknown | No supporting public source located. |
| `$["beta_settings"]["hermes_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of hermes (unidentified feature); current access, rollout completion, and precedence are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["hippo_in_chat_allowed"]` | `boolean` | Allow marker for an unidentified hippo capability within chat. | Unknown | No supporting public source located. |
| `$["beta_settings"]["hive"]` | `boolean` | Opaque feature identifier; no product mapping has been verified. | Unknown | No supporting public source located. |
| `$["beta_settings"]["hive_knowledge_retrieval"]` | `boolean` | Knowledge-retrieval subfeature of the unidentified hive feature; product mapping is unknown. | Unknown | No supporting public source located. |
| `$["beta_settings"]["include_user_identifier_in_survey_download"]` | `boolean` | Including user identifiers in a downloadable survey report; identifier format is unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["legacy_models"]` | `boolean` | Access to older models; this flag does not enumerate models or prove current model availability. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings"]["library_sharing_enabled"]` | `boolean` | Availability of sharing Library content with others. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["library_sharing_ga_opt_out"]` | `boolean` | Opt-out marker for a Library-sharing general-availability rollout; not necessarily an effective permission. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["library_sharing_management"]` | `boolean` | Ability to manage Library sharing configuration or permissions; distinct from consuming shared content. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["library_workspace_link_sharing"]` | `boolean` | Sharing Library content through links scoped to the workspace. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["m3m_ga_opt_out"]` | `boolean` | Rollout opt-out marker for opaque identifier m3m; the underlying product is unknown. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["m3m_workspace_enabled"]` | `boolean` | Workspace enable marker for opaque identifier m3m; no product mapping has been verified. | Unknown | No supporting public source located. |
| `$["beta_settings"]["orbit_enabled"]` | `boolean` | Enable marker for opaque identifier orbit; no product mapping has been verified. | Unknown | No supporting public source located. |
| `$["beta_settings"]["personal_access_tokens"]` | `boolean` | Availability of personal access token functionality; this boolean is not itself a token. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["plugins"]` | `boolean` | Availability of plugins; installation policy and individual app permissions can be separate. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["project_connector_scopes"]` | `boolean` | Connector access scoped to individual projects; scope semantics are unverified. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["project_group_chats"]` | `boolean` | Group-chat capability associated with projects; exact collaboration behavior is unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["project_group_chats_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of project group chats; current access, rollout completion, and precedence are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["project_sharing"]` | `boolean` | Ability to share projects with other people; eligible recipients and permission levels are unverified. | Inferred from name | [OpenAI projects and sharing](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings"]["project_sharing_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of project sharing; current access, rollout completion, and precedence are unverified. | Inferred from name | [OpenAI projects and sharing](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings"]["salute"]` | `boolean` | Opaque feature identifier; no product mapping has been verified. | Unknown | No supporting public source located. |
| `$["beta_settings"]["salute_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of salute (unidentified feature); current access, rollout completion, and precedence are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["sites"]` | `boolean` | Access to Sites, the site-creation feature; publishing permissions may be separate. | Inferred from name | [OpenAI Sites workspace controls](https://help.openai.com/en/articles/20001338-managing-chatgpt-sites-for-your-workspace) (product context; key mapping unverified) |
| `$["beta_settings"]["sites_ga_opt_out"]` | `boolean` | Opt-out marker for the Sites general-availability rollout; not proof of effective access. | Inferred from name | [OpenAI Sites workspace controls](https://help.openai.com/en/articles/20001338-managing-chatgpt-sites-for-your-workspace) (product context; key mapping unverified) |
| `$["beta_settings"]["skills"]` | `boolean` | Availability of skills, reusable task instructions or resources; upload and sharing permissions may be separate. | Inferred from name | [OpenAI skills and workspace permissions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/) (product context; key mapping unverified) |
| `$["beta_settings"]["skills_ga_opt_out"]` | `boolean` | Opt-out marker for general-availability rollout of skills; current access, rollout completion, and precedence are unverified. | Inferred from name | [OpenAI skills and workspace permissions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/) (product context; key mapping unverified) |
| `$["beta_settings"]["sunshine"]` | `boolean` | Opaque feature identifier; no product mapping has been verified. | Unknown | No supporting public source located. |
| `$["beta_settings"]["task_suggestions_enabled"]` | `boolean` | Availability of suggested tasks in a client or product surface; generation rules are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["training_allowed"]` | `boolean` | Whether training use is allowed in some scope; this flag alone does not establish the full contractual data-use policy or actual training use. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["unified_container_internet_egress"]` | `boolean` | Outbound internet access for a unified execution container; which runtimes it covers is unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["video_screen_sharing"]` | `boolean` | Availability of video or screen-sharing input; supported clients are not established by this flag. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["wham_access"]` | `boolean` | Access flag for opaque identifier wham; no product mapping is verified. | Unknown | No supporting public source located. |
| `$["beta_settings"]["wham_local_access"]` | `boolean` | Local-access variant of opaque identifier wham; no product mapping is verified. | Unknown | No supporting public source located. |
| `$["beta_settings"]["windows_computer_use"]` | `boolean` | The source author reports that the installed Windows client checks this key for Computer Use. No equivalent Mac key has been verified; client version and code evidence are not published here. | Confirmed | Source-author report about the installed Windows client; not independently reproduced in this repository. |
| `$["beta_settings"]["workspace_chat_history_limit"]` | `boolean` | Whether a workspace chat-history limit applies; it does not specify the limit or establish a retention duration. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["workspace_fedramp_banner"]` | `boolean` | Display of a workspace FedRAMP-related banner; not evidence of compliance certification. | Inferred from name | No supporting public source located. |
| `$["beta_settings"]["workspace_gpt_apps"]` | `boolean` | Whether workspace-created GPTs may use apps; third-party GPT rules may differ. | Inferred from name | [OpenAI GPT access controls](https://help.openai.com/en/articles/8555535-managing-gpt-access-in-enterprise-and-edu-workspaces) (product context; key mapping unverified) |
| `$["beta_settings"]["workspace_gpt_custom_actions"]` | `boolean` | Whether workspace-created GPTs may use custom actions that call external services. | Inferred from name | [OpenAI GPT access controls](https://help.openai.com/en/articles/8555535-managing-gpt-access-in-enterprise-and-edu-workspaces) (product context; key mapping unverified) |
| `$["beta_settings"]["workspace_plugin_publishing"]` | `boolean` | Ability to publish plugins for workspace use; publishing and installing are separate actions. | Inferred from name | [OpenAI app administration](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps) (product context; key mapping unverified) |
| `$["beta_settings"]["workspace_policy"]` | `boolean` | Display or availability of workspace-provided AI policy guidance. | Inferred from name | [OpenAI workspace controls](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) (product context; key mapping unverified) |
| `$["beta_settings"]["workspace_policy_work_home"]` | `boolean` | Display or application of workspace policy guidance in the Work home surface. | Inferred from name | [OpenAI workspace controls](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) (product context; key mapping unverified) |

## beta_settings_dict

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["beta_settings_dict"]` | `object` | Container of structured feature configuration, including role-policy maps and Library settings. | Inferred from name | No supporting public source located. |
| `$["beta_settings_dict"]["admin_preview_gpt_6_1_terra"]` | `object` | Structured preview role-policy map for the preview identified as gpt_6_1_terra; this name does not establish public model availability. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings_dict"]["admin_preview_gpt_6_1_terra"]["*"]` | `string` | Policy state under a redacted role-map key. All role identifiers, including built-in role keys, collapse to this path; assignment and policy values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings_dict"]["admin_preview_library_sharing"]` | `object` | Structured preview role-policy map for Library sharing. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings_dict"]["admin_preview_library_sharing"]["*"]` | `string` | Policy state under a redacted role-map key. All role identifiers, including built-in role keys, collapse to this path; assignment and policy values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings_dict"]["admin_preview_team_create"]` | `object` | Structured preview role-policy map for team creation. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings_dict"]["admin_preview_team_create"]["*"]` | `string` | Policy state under a redacted role-map key. All role identifiers, including built-in role keys, collapse to this path; assignment and policy values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["beta_settings_dict"]["library_sharing_admin_configuration"]` | `object` | Configuration recording administrator setup of Library sharing. | Inferred from name | No supporting public source located. |
| `$["beta_settings_dict"]["library_sharing_admin_configuration"]["configured"]` | `string` | Marker for whether Library sharing has been configured. The observed JSON type is string, not boolean; parsing rules are unverified. | Inferred from name | No supporting public source located. |
| `$["beta_settings_dict"]["library_sharing_control_mode"]` | `object` | Structured configuration selecting how Library sharing is governed. | Inferred from name | No supporting public source located. |
| `$["beta_settings_dict"]["library_sharing_control_mode"]["mode"]` | `string` | Library-sharing governance selector; complete mode enum and precedence over the top-level field are unverified. | Inferred from name | No supporting public source located. |

## beta_settings_str

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["beta_settings_str"]` | `object` | Container whose name suggests string-valued beta configuration; the empty object provides no member-type evidence. | Inferred from name | No supporting public source located. |

## composer_predictions_launched

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["composer_predictions_launched"]` | `boolean` | Launch-state marker for prompt-composer predictions; which clients and prediction behavior it covers is unverified. | Inferred from name | No supporting public source located. |

## conversation_ttl

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["conversation_ttl"]` | `null` | Conversation lifetime or retention-related setting; null establishes neither a duration nor unlimited retention. Units are unverified. | Inferred from name | No supporting public source located. |

## custom_permission_inheritance_enabled

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["custom_permission_inheritance_enabled"]` | `boolean` | Whether custom permissions may inherit another policy state; exact inheritance rules for this field are unverified. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |

## default_seat_type

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["default_seat_type"]` | `null` | Seat category used by default for provisioning; null does not identify a seat type or its representation. | Inferred from name | [OpenAI workspace membership and discovery](https://help.openai.com/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business) (product context; key mapping unverified) |

## desktop_app_beta_policy

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["desktop_app_beta_policy"]` | `string` | Desktop beta-client access policy; accepted policy values and platform scope are unverified. | Inferred from name | No supporting public source located. |

## disable_account_switching

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["disable_account_switching"]` | `boolean` | Restriction on switching accounts; precedence relative to enable_account_switching is unverified. | Inferred from name | [OpenAI workspace controls](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) (product context; key mapping unverified) |

## enable_account_switching

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["enable_account_switching"]` | `boolean` | Availability of account switching; precedence relative to disable_account_switching is unverified. | Inferred from name | [OpenAI workspace controls](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) (product context; key mapping unverified) |

## file_library_auto_reference_admin_control_retired

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["file_library_auto_reference_admin_control_retired"]` | `boolean` | Retirement state of an admin control for automatic Library file referencing; not necessarily the state of file referencing itself. | Inferred from name | No supporting public source located. |

## library_sharing_control_mode

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["library_sharing_control_mode"]` | `string` | Selector for how Library sharing is governed; precedence over similarly named nested configuration is unverified. | Inferred from name | No supporting public source located. |

## member_profile_activity_enabled

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["member_profile_activity_enabled"]` | `boolean` | Availability of activity information within member profiles; which activity is exposed is unverified. | Inferred from name | No supporting public source located. |

## member_profiles_enabled

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["member_profiles_enabled"]` | `boolean` | Availability of member profiles in workspace surfaces. | Inferred from name | No supporting public source located. |

## member_profiles_sharing

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["member_profiles_sharing"]` | `string` | Audience or sharing scope for member profile information; accepted values are unverified. | Inferred from name | No supporting public source located. |

## model_permission_preferences

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["model_permission_preferences"]` | `object` | Map linking model-related preference identifiers to permission identifiers; how the preferences are evaluated is unverified. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["model_permission_preferences"]["ultra-fast-mode"]` | `string` | Permission-identifier mapping for an ultra-fast mode preference; supported models and enforcement are unverified. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |

## orbit_rollout_eligible

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["orbit_rollout_eligible"]` | `boolean` | Rollout eligibility for opaque identifier orbit; eligibility alone would not prove access. | Inferred from name | No supporting public source located. |

## orbit_uses_workspace_setting

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["orbit_uses_workspace_setting"]` | `boolean` | Whether opaque identifier orbit follows a workspace setting; the referenced setting is unknown. | Inferred from name | No supporting public source located. |

## owner_setup_join_preference_confirmed

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["owner_setup_join_preference_confirmed"]` | `boolean` | Whether an owner has confirmed a joining preference during setup; does not identify the choice. | Inferred from name | No supporting public source located. |

## permissions

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["permissions"]` | `array` | Permission identifiers returned for this response. Whether they represent effective caller permissions, workspace eligibility, or another scope is unverified. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["permissions"][]` | `string` | An individual permission identifier string. Naming conventions may encode a resource, action, model, or feature; actual permission values and their order are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |

## plugin_incentive_campaigns

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["plugin_incentive_campaigns"]` | `array` | Collection of plugin incentive campaigns; the empty array provides no evidence of campaign item structure. | Inferred from name | No supporting public source located. |

## plugin_incentives_ui_enabled

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["plugin_incentives_ui_enabled"]` | `boolean` | Visibility or availability of a plugin-incentives user interface. | Inferred from name | No supporting public source located. |

## public_display_name

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["public_display_name"]` | `null` | Public or discoverable workspace display name; null does not establish that discovery is disabled. | Inferred from name | [OpenAI workspace membership and discovery](https://help.openai.com/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business) (product context; key mapping unverified) |

## role_summaries

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["role_summaries"]` | `array` | Collection of role descriptions and related permission/assignment information; inclusion does not establish a particular member-role assignment. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]` | `object` | One role summary object, not evidence that a particular individual holds that role. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]["assignment_sources"]` | `array` | Sources or principals associated with assignment of this role; precise membership semantics are unverified. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]["assignment_sources"][]` | `object` | One assignment-source record; actual membership and principal values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]["assignment_sources"][]["principal_id"]` | `string` | Identifier of a principal associated with the assignment source; the actual identifier is omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]["assignment_sources"][]["principal_type"]` | `string` | Category of the assignment-source principal; the full category set is unverified. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]["id"]` | `string` | Identifier of the summarized role; may encode workspace information, so actual values are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]["metadata"]` | `null` | Additional role metadata; the observed null reveals no metadata structure. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]["name"]` | `string` | Human-readable role label; actual role names are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]["permissions"]` | `array` | Permission identifiers associated with this role summary; not proof of effective access after other policy checks. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |
| `$["role_summaries"][]["permissions"][]` | `string` | One permission identifier associated with this role; actual values and ordering are omitted. | Inferred from name | [OpenAI role-based access control](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) (product context; key mapping unverified) |

## search_restrictions

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["search_restrictions"]` | `string` | Selector for search restrictions; search surfaces and the complete enum are unverified. | Inferred from name | [OpenAI web search](https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt) (product context; key mapping unverified) |

## seat_type_credit_limits

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["seat_type_credit_limits"]` | `null` | Credit-limit configuration associated with seat types; null reveals no numeric unit or nested structure. | Inferred from name | No supporting public source located. |

## settings

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["settings"]` | `object` | General settings container; no child keys were present in the observed object. | Inferred from name | No supporting public source located. |

## share_settings

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["share_settings"]` | `object` | Container for separate chat-sharing and GPT-sharing policies. | Inferred from name | [OpenAI workspace controls](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) (product context; key mapping unverified) |
| `$["share_settings"]["chat_share_setting"]` | `string` | Policy selecting allowed chat-sharing audiences; complete enum and enforcement are unverified. | Inferred from name | [OpenAI workspace controls](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) (product context; key mapping unverified) |
| `$["share_settings"]["gpt_share_setting"]` | `string` | Policy selecting allowed GPT-sharing audiences; complete enum and enforcement are unverified. | Inferred from name | [OpenAI GPT access controls](https://help.openai.com/en/articles/8555535-managing-gpt-access-in-enterprise-and-edu-workspaces) (product context; key mapping unverified) |

## support_workspace_discovery

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["support_workspace_discovery"]` | `boolean` | Whether workspace discovery is supported or available, distinct from the configured discoverability flag. | Inferred from name | [OpenAI workspace membership and discovery](https://help.openai.com/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business) (product context; key mapping unverified) |

## unified_workspace_name

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["unified_workspace_name"]` | `boolean` | Name unification behavior across workspace surfaces; scope and migration semantics are unverified. | Inferred from name | No supporting public source located. |

## usage_limit_increase_request

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["usage_limit_increase_request"]` | `object` | Configuration for instructions and a destination used to request a usage-limit increase; it is not a record that a request was sent. | Inferred from name | No supporting public source located. |
| `$["usage_limit_increase_request"]["instructions"]` | `string` | Text shown to explain how to request a usage-limit increase; actual organization instructions are omitted. | Inferred from name | No supporting public source located. |
| `$["usage_limit_increase_request"]["kind"]` | `string` | Discriminator selecting the usage-limit request workflow; the full set of kinds is unknown. | Inferred from name | No supporting public source located. |
| `$["usage_limit_increase_request"]["request_url"]` | `string` | Destination URL for a usage-limit increase request; actual organization URL is omitted. | Inferred from name | No supporting public source located. |

## use_workspace_name_for_discovery

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["use_workspace_name_for_discovery"]` | `boolean` | Whether workspace discovery displays the workspace name rather than a separate display name. | Inferred from name | [OpenAI workspace membership and discovery](https://help.openai.com/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business) (product context; key mapping unverified) |

## workspace_banner_available

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["workspace_banner_available"]` | `boolean` | Availability of a workspace banner; does not establish whether a banner is configured or visible. | Inferred from name | No supporting public source located. |

## workspace_discoverable

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["workspace_discoverable"]` | `boolean` | Whether eligible people can discover the workspace when joining; domain/eligibility rules are separate. | Inferred from name | [OpenAI workspace membership and discovery](https://help.openai.com/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business) (product context; key mapping unverified) |

## workspace_id

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["workspace_id"]` | `string` | Identifier of the workspace associated with the response; the actual identifier is omitted. | Inferred from name | [OpenAI workspace controls](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) (product context; key mapping unverified) |

## workspace_referrals_enabled

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["workspace_referrals_enabled"]` | `boolean` | Availability of workspace referrals or referral actions; program rules are unverified. | Inferred from name | No supporting public source located. |

## workspace_referrals_enabled_visible

| Full JSON path | Observed type | Meaning | Status | Evidence / context |
|---|---|---|---|---|
| `$["workspace_referrals_enabled_visible"]` | `boolean` | Visibility of the control or UI for workspace referrals, distinct from enabling referrals. | Inferred from name | No supporting public source located. |
