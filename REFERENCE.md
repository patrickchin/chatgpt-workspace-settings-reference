# Observed key reference

One response observed on 2026-11-19. This is an unofficial snapshot, not a complete schema or a statement of defaults. The original values are intentionally omitted.

`[]` denotes a representative array item. `*` denotes a redacted role-like map key. `null` and empty collections reveal no underlying schema type beyond the observed JSON value.

## `access_request`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["access_request"]` | `null` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `access_token_max_ttl`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["access_token_max_ttl"]` | `integer` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `admin_preview_launch_defaults`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["admin_preview_launch_defaults"]` | `object` | Container or policy field named `admin_preview_launch_defaults`; precise backend semantics are not documented here. | Inferred from name | — |
| `$["admin_preview_launch_defaults"]["admin_preview_gpt_6_2_astra"]` | `string` | Name suggests a admin preview gpt 6 2 astra setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_defaults"]["admin_preview_gpt_6_2_sol"]` | `string` | Name suggests a admin preview gpt 6 2 sol setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_defaults"]["admin_preview_library_sharing"]` | `string` | Name suggests a admin preview library sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_defaults"]["admin_preview_library_workspace_link_sharing"]` | `string` | Name suggests a admin preview library workspace link sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_defaults"]["admin_preview_team_automations"]` | `string` | Name suggests a admin preview team automations setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_defaults"]["admin_preview_team_create"]` | `string` | Name suggests a admin preview team create setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `admin_preview_launch_settings`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["admin_preview_launch_settings"]` | `object` | Container or policy field named `admin_preview_launch_settings`; precise backend semantics are not documented here. | Inferred from name | — |
| `$["admin_preview_launch_settings"]["admin_preview_gpt_6_1_terra"]` | `object` | Name suggests a admin preview gpt 6 1 terra setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_settings"]["admin_preview_gpt_6_1_terra"]["*"]` | `string` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_launch_settings"]["admin_preview_gpt_6_1_terra"]["role-workspace-member"]` | `string` | Name suggests a role-workspace-member setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_settings"]["admin_preview_library_sharing"]` | `object` | Name suggests a admin preview library sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_settings"]["admin_preview_library_sharing"]["role-workspace-member"]` | `string` | Name suggests a role-workspace-member setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_settings"]["admin_preview_team_create"]` | `object` | Name suggests a admin preview team create setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_launch_settings"]["admin_preview_team_create"]["*"]` | `string` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_launch_settings"]["admin_preview_team_create"]["role-workspace-member"]` | `string` | Name suggests a role-workspace-member setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `admin_preview_matching`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["admin_preview_matching"]` | `object` | Container or policy field named `admin_preview_matching`; precise backend semantics are not documented here. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]` | `object` | Name suggests a admin preview gpt 6 2 astra setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["can_edit_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["mode"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["revision"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["saved_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_astra"]["show_sync_toggle"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]` | `object` | Name suggests a admin preview gpt 6 2 sol setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["can_edit_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["mode"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["revision"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["saved_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_gpt_6_2_sol"]["show_sync_toggle"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]` | `object` | Name suggests a admin preview library sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["can_edit_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["mode"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["revision"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["saved_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_library_sharing"]["show_sync_toggle"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]` | `object` | Name suggests a admin preview library workspace link sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["can_edit_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["mode"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["revision"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["saved_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_library_workspace_link_sharing"]["show_sync_toggle"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_team_automations"]` | `object` | Name suggests a admin preview team automations setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["can_edit_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["mode"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["revision"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["saved_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_team_automations"]["show_sync_toggle"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_team_create"]` | `object` | Name suggests a admin preview team create setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_team_create"]["can_edit_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_team_create"]["mode"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_team_create"]["revision"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["admin_preview_matching"]["admin_preview_team_create"]["saved_sync"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["admin_preview_matching"]["admin_preview_team_create"]["show_sync_toggle"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |

## `admin_work_local_enabled`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["admin_work_local_enabled"]` | `boolean` | Name suggests a admin work local enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `admin_work_mode_enabled`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["admin_work_mode_enabled"]` | `boolean` | Name suggests a admin work mode enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `allow_external_domain_invites`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["allow_external_domain_invites"]` | `boolean` | Name suggests a allow external domain invites setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `allow_third_party_gpts`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["allow_third_party_gpts"]` | `string` | Name suggests a allow third party gpts setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `allowed_custom_actions_domains`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["allowed_custom_actions_domains"]` | `null` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `allowed_web_search_domains`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["allowed_web_search_domains"]` | `null` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `auto_accept_requests`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["auto_accept_requests"]` | `boolean` | Workspace identity or discovery-related field, based on the documented workspace controls. | Confirmed | [OpenAI Business roles and discovery](https://help.openai.com/en/articles/8542216-managing-workspaces-people-and-access-in-chatgpt-business) |

## `auto_approve_seat_upgrades`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["auto_approve_seat_upgrades"]` | `boolean` | Name suggests a auto approve seat upgrades setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `auto_join_pending_requests_enabled`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["auto_join_pending_requests_enabled"]` | `boolean` | Name suggests a auto join pending requests enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `available_admin_preview_features`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["available_admin_preview_features"]` | `object` | Container or policy field named `available_admin_preview_features`; precise backend semantics are not documented here. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_gpt_6_2_astra"]` | `array` | Name suggests a admin preview gpt 6 2 astra setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_gpt_6_2_astra"][]` | `string` | Name suggests a admin preview gpt 6 2 astra setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_gpt_6_2_sol"]` | `array` | Name suggests a admin preview gpt 6 2 sol setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_gpt_6_2_sol"][]` | `string` | Name suggests a admin preview gpt 6 2 sol setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_library_sharing"]` | `array` | Name suggests a admin preview library sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_library_sharing"][]` | `string` | Name suggests a admin preview library sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_library_workspace_link_sharing"]` | `array` | Name suggests a admin preview library workspace link sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_library_workspace_link_sharing"][]` | `string` | Name suggests a admin preview library workspace link sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_team_automations"]` | `array` | Name suggests a admin preview team automations setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_team_automations"][]` | `string` | Name suggests a admin preview team automations setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_team_create"]` | `array` | Name suggests a admin preview team create setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["available_admin_preview_features"]["admin_preview_team_create"][]` | `string` | Name suggests a admin preview team create setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `beta_settings`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["beta_settings"]` | `object` | Container or policy field named `beta_settings`; precise backend semantics are not documented here. | Inferred from name | — |
| `$["beta_settings"]["agent_mode"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["allow_computer_history"]` | `boolean` | Name suggests a allow computer history setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["app_pairing"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["aura"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["aura_ga_opt_out"]` | `boolean` | Name suggests a aura ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["auto_scim_groups_to_teams"]` | `boolean` | Name suggests a auto scim groups to teams setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["basispoints_ga_opt_out"]` | `boolean` | Name suggests a basispoints ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["basispoints_powerpoint_ga_opt_out"]` | `boolean` | Name suggests a basispoints powerpoint ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["browsing"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["canvas"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["canvas_code_execution"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["canvas_code_network_access"]` | `boolean` | Name suggests a canvas code network access setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["client_application_apple"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["client_application_apple_mdm_required"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["code_interpreter"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["codex_admin"]` | `boolean` | Name suggests a codex admin setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_agent_network_access"]` | `boolean` | Name suggests a codex agent network access setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_code_attribution_analytics"]` | `boolean` | Name suggests a codex code attribution analytics setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_composer_predictions"]` | `boolean` | Name suggests a codex composer predictions setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_device_code_auth"]` | `boolean` | Name suggests a codex device code auth setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_git_attribution"]` | `boolean` | Name suggests a codex git attribution setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_remote_control"]` | `boolean` | Name suggests a codex remote control setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_security"]` | `boolean` | Name suggests a codex security setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_security_admin"]` | `boolean` | Name suggests a codex security admin setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_slack_posting"]` | `boolean` | Name suggests a codex slack posting setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["codex_usage_leaderboard"]` | `boolean` | Name suggests a codex usage leaderboard setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["context_connector_confluence"]` | `boolean` | Name suggests a context connector confluence setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["context_connector_gdrive"]` | `boolean` | Name suggests a context connector gdrive setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["context_connector_java"]` | `boolean` | Name suggests a context connector java setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["context_connector_notion"]` | `boolean` | Name suggests a context connector notion setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["context_connector_o365_business"]` | `boolean` | Name suggests a context connector o365 business setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["context_connector_o365_personal"]` | `boolean` | Name suggests a context connector o365 personal setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["context_connector_slack"]` | `boolean` | Name suggests a context connector slack setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["dalle"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["deep_research"]` | `boolean` | Name suggests a deep research setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["developer_mode"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["enable_conversation_classifier"]` | `boolean` | Name suggests a enable conversation classifier setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["enable_free_trial_seats"]` | `boolean` | Name suggests a enable free trial seats setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["enable_message_feedback"]` | `boolean` | Name suggests a enable message feedback setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["enable_plugins"]` | `boolean` | Name suggests a enable plugins setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["enable_value_survey_campaign"]` | `boolean` | Name suggests a enable value survey campaign setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["enhanced_citations"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["file_library_auto_reference"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["file_library_auto_reference_ga_opt_out"]` | `boolean` | Name suggests a file library auto reference ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["flora_ga_opt_out"]` | `boolean` | Name suggests a flora ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["gpt51_ga_opt_out"]` | `boolean` | Name suggests a gpt51 ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["hermes"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["hermes_ga_opt_out"]` | `boolean` | Name suggests a hermes ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["hippo_in_chat_allowed"]` | `boolean` | Name suggests a hippo in chat allowed setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["hive"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["hive_knowledge_retrieval"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["include_user_identifier_in_survey_download"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["legacy_models"]` | `boolean` | Name suggests a legacy models setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["library_sharing_enabled"]` | `boolean` | Name suggests a library sharing enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["library_sharing_ga_opt_out"]` | `boolean` | Name suggests a library sharing ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["library_sharing_management"]` | `boolean` | Name suggests a library sharing management setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["library_workspace_link_sharing"]` | `boolean` | Name suggests a library workspace link sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["m3m_ga_opt_out"]` | `boolean` | Name suggests a m3m ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["m3m_workspace_enabled"]` | `boolean` | Name suggests a m3m workspace enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["orbit_enabled"]` | `boolean` | Name suggests a orbit enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["personal_access_tokens"]` | `boolean` | Name suggests a personal access tokens setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["plugins"]` | `boolean` | Name suggests a plugins setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["project_connector_scopes"]` | `boolean` | Name suggests a project connector scopes setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["project_group_chats"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["project_group_chats_ga_opt_out"]` | `boolean` | Name suggests a project group chats ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["project_sharing"]` | `boolean` | Name suggests a project sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["project_sharing_ga_opt_out"]` | `boolean` | Name suggests a project sharing ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["salute"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["salute_ga_opt_out"]` | `boolean` | Name suggests a salute ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["sites"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["sites_ga_opt_out"]` | `boolean` | Name suggests a sites ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["skills"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["skills_ga_opt_out"]` | `boolean` | Name suggests a skills ga opt out setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["sunshine"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["task_suggestions_enabled"]` | `boolean` | Name suggests a task suggestions enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["training_allowed"]` | `boolean` | Name suggests a training allowed setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["unified_container_internet_egress"]` | `boolean` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings"]["video_screen_sharing"]` | `boolean` | Name suggests a video screen sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["wham_access"]` | `boolean` | Name suggests a wham access setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["wham_local_access"]` | `boolean` | Name suggests a wham local access setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["windows_computer_use"]` | `boolean` | Feature-availability flag checked by the installed Windows client, as observed by the source author; no Mac equivalent is verified. | Confirmed | — |
| `$["beta_settings"]["workspace_chat_history_limit"]` | `boolean` | Name suggests a workspace chat history limit setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["workspace_fedramp_banner"]` | `boolean` | Name suggests a workspace fedramp banner setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["workspace_gpt_apps"]` | `boolean` | Name suggests a workspace gpt apps setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["workspace_gpt_custom_actions"]` | `boolean` | Name suggests a workspace gpt custom actions setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["workspace_plugin_publishing"]` | `boolean` | Name suggests a workspace plugin publishing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["workspace_policy"]` | `boolean` | Name suggests a workspace policy setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings"]["workspace_policy_work_home"]` | `boolean` | Name suggests a workspace policy work home setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `beta_settings_dict`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["beta_settings_dict"]` | `object` | Container or policy field named `beta_settings_dict`; precise backend semantics are not documented here. | Inferred from name | — |
| `$["beta_settings_dict"]["admin_preview_gpt_6_1_terra"]` | `object` | Name suggests a admin preview gpt 6 1 terra setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings_dict"]["admin_preview_gpt_6_1_terra"]["*"]` | `string` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings_dict"]["admin_preview_gpt_6_1_terra"]["role-workspace-member"]` | `string` | Name suggests a role-workspace-member setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings_dict"]["admin_preview_library_sharing"]` | `object` | Name suggests a admin preview library sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings_dict"]["admin_preview_library_sharing"]["role-workspace-member"]` | `string` | Name suggests a role-workspace-member setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings_dict"]["admin_preview_team_create"]` | `object` | Name suggests a admin preview team create setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings_dict"]["admin_preview_team_create"]["*"]` | `string` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["beta_settings_dict"]["admin_preview_team_create"]["role-workspace-member"]` | `string` | Name suggests a role-workspace-member setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings_dict"]["library_sharing_admin_configuration"]` | `object` | Name suggests a library sharing admin configuration setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings_dict"]["library_sharing_admin_configuration"]["configured"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["beta_settings_dict"]["library_sharing_control_mode"]` | `object` | Name suggests a library sharing control mode setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["beta_settings_dict"]["library_sharing_control_mode"]["mode"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `beta_settings_str`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["beta_settings_str"]` | `object` | Container or policy field named `beta_settings_str`; precise backend semantics are not documented here. | Inferred from name | — |

## `composer_predictions_launched`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["composer_predictions_launched"]` | `boolean` | Name suggests a composer predictions launched setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `conversation_ttl`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["conversation_ttl"]` | `null` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `custom_permission_inheritance_enabled`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["custom_permission_inheritance_enabled"]` | `boolean` | Name suggests a custom permission inheritance enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `default_seat_type`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["default_seat_type"]` | `null` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `desktop_app_beta_policy`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["desktop_app_beta_policy"]` | `string` | Container or policy field named `desktop_app_beta_policy`; precise backend semantics are not documented here. | Inferred from name | — |

## `disable_account_switching`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["disable_account_switching"]` | `boolean` | Name suggests a disable account switching setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `enable_account_switching`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["enable_account_switching"]` | `boolean` | Name suggests a enable account switching setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `file_library_auto_reference_admin_control_retired`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["file_library_auto_reference_admin_control_retired"]` | `boolean` | Name suggests a file library auto reference admin control retired setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `library_sharing_control_mode`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["library_sharing_control_mode"]` | `string` | Name suggests a library sharing control mode setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `member_profile_activity_enabled`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["member_profile_activity_enabled"]` | `boolean` | Name suggests a member profile activity enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `member_profiles_enabled`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["member_profiles_enabled"]` | `boolean` | Name suggests a member profiles enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `member_profiles_sharing`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["member_profiles_sharing"]` | `string` | Name suggests a member profiles sharing setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `model_permission_preferences`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["model_permission_preferences"]` | `object` | Container or policy field named `model_permission_preferences`; precise backend semantics are not documented here. | Inferred from name | — |
| `$["model_permission_preferences"]["ultra-fast-mode"]` | `string` | No reliable meaning established from the field name or cited documentation. | Unknown | — |

## `orbit_rollout_eligible`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["orbit_rollout_eligible"]` | `boolean` | Name suggests a orbit rollout eligible setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `orbit_uses_workspace_setting`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["orbit_uses_workspace_setting"]` | `boolean` | Name suggests a orbit uses workspace setting setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `owner_setup_join_preference_confirmed`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["owner_setup_join_preference_confirmed"]` | `boolean` | Name suggests a owner setup join preference confirmed setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `permissions`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["permissions"]` | `array` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |
| `$["permissions"][]` | `string` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |

## `plugin_incentive_campaigns`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["plugin_incentive_campaigns"]` | `array` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `plugin_incentives_ui_enabled`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["plugin_incentives_ui_enabled"]` | `boolean` | Name suggests a plugin incentives ui enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `public_display_name`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["public_display_name"]` | `null` | Workspace identity or discovery-related field, based on the documented workspace controls. | Confirmed | [OpenAI Business roles and discovery](https://help.openai.com/en/articles/8542216-managing-workspaces-people-and-access-in-chatgpt-business) |

## `role_summaries`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["role_summaries"]` | `array` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |
| `$["role_summaries"][]` | `object` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |
| `$["role_summaries"][]["assignment_sources"]` | `array` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |
| `$["role_summaries"][]["assignment_sources"][]` | `object` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |
| `$["role_summaries"][]["assignment_sources"][]["principal_id"]` | `string` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |
| `$["role_summaries"][]["assignment_sources"][]["principal_type"]` | `string` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |
| `$["role_summaries"][]["id"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["role_summaries"][]["metadata"]` | `null` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["role_summaries"][]["name"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["role_summaries"][]["permissions"]` | `array` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |
| `$["role_summaries"][]["permissions"][]` | `string` | Permission or role-related data; the response shape alone does not define the exact authorization semantics. | Confirmed | [OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) |

## `search_restrictions`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["search_restrictions"]` | `string` | Name suggests a search restrictions setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `seat_type_credit_limits`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["seat_type_credit_limits"]` | `null` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `settings`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["settings"]` | `object` | Container or policy field named `settings`; precise backend semantics are not documented here. | Inferred from name | — |

## `share_settings`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["share_settings"]` | `object` | Name suggests a share settings setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
| `$["share_settings"]["chat_share_setting"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["share_settings"]["gpt_share_setting"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `support_workspace_discovery`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["support_workspace_discovery"]` | `boolean` | Name suggests a support workspace discovery setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `unified_workspace_name`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["unified_workspace_name"]` | `boolean` | Name suggests a unified workspace name setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `usage_limit_increase_request`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["usage_limit_increase_request"]` | `object` | No reliable meaning established from the field name or cited documentation. | Unknown | — |
| `$["usage_limit_increase_request"]["instructions"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["usage_limit_increase_request"]["kind"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |
| `$["usage_limit_increase_request"]["request_url"]` | `string` | The field name indicates the general data concept; its backend-specific effect is not established by this response. | Inferred from name | — |

## `use_workspace_name_for_discovery`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["use_workspace_name_for_discovery"]` | `boolean` | Workspace identity or discovery-related field, based on the documented workspace controls. | Confirmed | [OpenAI Business roles and discovery](https://help.openai.com/en/articles/8542216-managing-workspaces-people-and-access-in-chatgpt-business) |

## `workspace_banner_available`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["workspace_banner_available"]` | `boolean` | Name suggests a workspace banner available setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `workspace_discoverable`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["workspace_discoverable"]` | `boolean` | Workspace identity or discovery-related field, based on the documented workspace controls. | Confirmed | [OpenAI Business roles and discovery](https://help.openai.com/en/articles/8542216-managing-workspaces-people-and-access-in-chatgpt-business) |

## `workspace_id`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["workspace_id"]` | `string` | Workspace identity or discovery-related field, based on the documented workspace controls. | Confirmed | [OpenAI Business roles and discovery](https://help.openai.com/en/articles/8542216-managing-workspaces-people-and-access-in-chatgpt-business) |

## `workspace_referrals_enabled`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["workspace_referrals_enabled"]` | `boolean` | Name suggests a workspace referrals enabled setting or feature flag; no specific server behavior is verified. | Inferred from name | — |

## `workspace_referrals_enabled_visible`

| Full JSON path | Observed type | Meaning | Status | Source |
|---|---|---|---|---|
| `$["workspace_referrals_enabled_visible"]` | `boolean` | Name suggests a workspace referrals enabled visible setting or feature flag; no specific server behavior is verified. | Inferred from name | — |
