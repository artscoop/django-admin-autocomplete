<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>
  artscoop / django-admin-autocomplete 
  / source  / admin_autocomplete_mixin.py
 &mdash; Bitbucket
</title>
  <link rel="icon" type="image/png" href="https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/img/favicon.png">
  <meta id="bb-canon-url" name="bb-canon-url" content="https://bitbucket.org">
  
  
<link rel="stylesheet" href="https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/compressed/css/fa9f0a1f936b.css" type="text/css" />

  <!--[if lt IE 9]><link rel="stylesheet" href="https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/css/aui/aui-ie.css" media="all"><![endif]-->
  <!--[if IE]><link rel="stylesheet" href="https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/css/aui-overrides-ie.css" media="all"><![endif]-->
  <meta name="description" content=""/>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Bitbucket" />
  
  <link href="/artscoop/django-admin-autocomplete/rss?token=4a5b46b5d6c73cb7159be90da10a7a28" rel="alternate nofollow" type="application/rss+xml" title="RSS feed for django-admin-autocomplete" />

</head>
<body class="aui-layout production ">
<script type="text/javascript" src="https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/compressed/js/e98deabf8a2e.js"></script>
<div id="page">
  <div id="wrapper">
    
    <header id="header" role="banner">
      <nav class="aui-header aui-dropdown2-trigger-group" role="navigation">
        <div class="aui-header-inner">
          <div class="aui-header-primary">
            <h1 class="aui-header-logo aui-header-logo-bitbucket">
              <a href="/" class="aui-nav-imagelink">
                <span class="aui-header-logo-device">Bitbucket</span>
              </a>
            </h1>
            <script id="repo-dropdown-template" type="text/html">
  

[[#hasViewed]]
  <div class="aui-dropdown2-section">
    <strong class="viewed">Recently viewed</strong>
    <ul class="aui-list-truncate">
      [[#viewed]]
        <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
          <a href="[[url]]" title="[[owner]]/[[name]]" class=" aui-icon-container">
            <img class="repo-avatar size16" src="[[{avatar}]]" alt="[[owner]]/[[name]] avatar"/>
            [[owner]] / [[name]]
          </a>
        </li>
      [[/viewed]]
    </ul>
  </div>
[[/hasViewed]]
[[#hasUpdated]]
<div class="aui-dropdown2-section">
  <strong class="updated">Recently updated</strong>
  <ul class="aui-list-truncate">
    [[#updated]]
    <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
      <a href="[[url]]" title="[[owner]]/[[name]]" class=" aui-icon-container">
        <img class="repo-avatar size16" src="[[{avatar}]]" alt="[[owner]]/[[name]] avatar"/>
        [[owner]] / [[name]]
      </a>
    </li>
    [[/updated]]
  </ul>
</div>
[[/hasUpdated]]

</script>
            <ul role="menu" class="aui-nav">
              
                <li>
                  <a href="https://bitbucket.org" id="dashboard-link">
                    Dashboard
                  </a>
                </li>
                <li>
                  <a class="aui-dropdown2-trigger aui-dropdown2-trigger selected"
                     aria-owns="repo-dropdown" aria-haspopup="true" href="/repo/mine " id="repositories-dropdown-trigger">
                    Repositories
                    <span class="aui-icon-dropdown"></span>
                  </a>
                  <nav id="repo-dropdown" class="aui-dropdown2 aui-style-default">
                    <div id="repo-dropdown-recent"></div>
                    <div class="aui-dropdown2-section">
                      <ul>
                        <li>
                          <a href="/repo/create" class="new-repository" id="create-repo-link">
                            Create repository
                          </a>
                        </li>
                        <li>
                          <a href="/repo/import" class="import-repository" id="import-repo-link">
                            Import repository
                          </a>
                        </li>
                      </ul>
                    </div>
                  </nav>
                </li>
              
            </ul>
          </div>
          <div class="aui-header-secondary">
            <ul role="menu" class="aui-nav">
              <li>
                <form action="/repo/all" method="get" class="aui-quicksearch">
                  <label for="search-query" class="assistive">owner/repository</label>
                  <input  id="search-query" class="search" type="text" placeholder="owner/repository" name="name">
                </form>
              </li>
              <li>
                <a class="aui-dropdown2-trigger"aria-controls="header-help-dropdown" aria-owns="header-help-dropdown"
                   aria-haspopup="true" data-container="#header .aui-header-inner" href="#header-help-dropdown">
                  <span class="aui-icon aui-icon-small aui-iconfont-help">Help</span><span class="aui-icon-dropdown"></span>
                </a>
                <nav id="header-help-dropdown" class="aui-dropdown2 aui-style-default aui-dropdown2-in-header" aria-hidden="true">
                  <div class="aui-dropdown2-section">
                    <ul>
                      <li><a href="https://confluence.atlassian.com/display/BITBUCKET/bitbucket+Documentation+Home" target="_blank">Documentation</a></li>
                      <li><a href="https://confluence.atlassian.com/display/BITBUCKET/bitbucket+101" target="_blank">Bitbucket 101</a></li>
                      <li><a href="https://confluence.atlassian.com/display/BBKB/Bitbucket+Knowledge+Base+Home" target="_blank">Knowledge Base</a></li>
                    </ul>
                  </div>
                  <div class="aui-dropdown2-section">
                    <ul>
                      <li><a href="https://answers.atlassian.com/tags/bitbucket/" target="_blank">Bitbucket on Atlassian Answers</a></li>
                      <li><a href="/support">Support</a></li>
                    </ul>
                  </div>
                </nav>
              </li>
              
                <li>
                  <a class="aui-dropdown2-trigger"
                     aria-owns="user-dropdown" aria-haspopup="true" data-container="#header .aui-header-inner"
                     href="/artscoop" title="artscoop" id="user-dropdown-trigger">
                    <div class="aui-avatar aui-avatar-small">
                        <div class="aui-avatar-inner">
                            <img src="https://secure.gravatar.com/avatar/2ac66487401fecdb194f7a0ae07dd8fd?d=https%3A%2F%2Fdwz7u9t8u8usb.cloudfront.net%2Fm%2Fa1fb05d05bb7%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&amp;s=32" alt="artscoop" height="24" width="24" />
                        </div>
                    </div>
                  </a>
                  <nav id="user-dropdown" class="aui-dropdown2 aui-style-default" aria-hidden="true">
                    <div class="aui-dropdown2-section">
                      <ul>
                        <li>
                          <a href="/artscoop" id="profile-link">View Profile</a>
                        </li>
                        <li>
                          <a href="/account/user/artscoop/" id="account-link">Manage Account</a>
                        </li>
                        <li>
                          <a href="/account/notifications/" id="inbox-link">Inbox <span id="inbox-unread-count"></span></a>
                        </li>
                        <li>
                          <a href="/account/signout/">Log out</a>
                        </li>
                      </ul>
                    </div>
                      <div class="aui-dropdown2-section" id="account-admin-links">
                        <strong>Teams</strong>
                          <ul class="aui-list-truncate">
                          </ul>
                        </div>
                      <div class="aui-dropdown2-section">
                          <ul>
                              <li>
                                  <a href="#general-invite" class='general-invite-link'>Invite a friend</a>
                              </li>
                          </ul>
                      </div>
                      
                      <div class="aui-dropdown2-section">
                        <ul>
                          <li>
                            <a href="/account/create-team/" id="create-team-link">Create Team</a>
                          </li>
                          <li>
                            <a href="/account/user/artscoop/convert-team/">Convert to Team</a>
                          </li>
                        </ul>
                      </div>
                    
                  </nav>
                </li>
              
            </ul>
          </div>
        </div>
      </nav>
    </header>
      <header id="account-warning" role="banner"
              class="aui-message-banner warning ">
        <div class="center-content">
          <span class="aui-icon aui-icon-warning"></span>
          <span class="message">
            
          </span>
        </div>
      </header>
    
      <header id="aui-message-bar">
        
      </header>
    
    
  <header id="repo-warning" role="banner" class="aui-message-banner warning">
    <div class="center-content">
      <span class="aui-icon aui-icon-warning"></span>
      <span class="message">
      </span>
    </div>
  </header>
  <script id="repo-warning-template" type="text/html">
  




  This repository's ownership is pending transfer to <a href="/[[username]]">[[username]]</a>.
  Visit the <a href="/artscoop/django-admin-autocomplete/admin/transfer">transfer repository page</a> to view more details.


</script>
  <header id="repo-header" class="subhead row">
    <div class="center-content">
      <div class="repo-summary">
        <a class="repo-avatar-link" href="/artscoop/django-admin-autocomplete">
          <span class="repo-avatar-container size64">
  <img alt="django-admin-autocomplete" src="https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/img/language-avatars/default_64.png"/>
</span>

          
        </a>
        <h1><a class="repo-link" href="/artscoop/django-admin-autocomplete">django-admin-autocomplete</a></h1>
        <ul class="repo-metadata clearfix">
          <li>
            <a class="user" href="/artscoop">
              <span class="icon user">User Icon</span>
              <span>artscoop</span>
            </a>
          </li>
          
          <li>
            <a class="fork-of" href="/tymofiy/django-admin-autocomplete">
              <span class="icon fork-of">Fork Icon</span>
              <span>Fork of django-admin-autocomplete</span>
            </a>
          </li>
          
          
          <li class="social">
            <a class="follow following" id="repo-follow"
               rel="nofollow"
               href="/artscoop/django-admin-autocomplete/follow">
              <span class="icon follow">Follow Icon</span>
              <span class="text">Following</span>
            </a>
          </li>
          
          <li class="social">
              <a class="invite" href="#invite" id="repo-invite-link">
                  <span class="icon invitation">Invitation Icon</span>
                  <span>Invite</span>
              </a>
              

<form class="aui" id="invite-form" method="post"
      action="/api/1.0/invitations/artscoop/django-admin-autocomplete"
      novalidate>
  <div class="error aui-message hidden">
    <span class="aui-icon icon-error"></span>
    <div class="message"></div>
  </div>
  <div class="field-group">
    <label for="id_email_address">Email address</label>
    <input type="email" id="id_email_address" name="email-address"
           class="text">
  </div>
  <div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='5ed63181c2ed3b5fd7f6d8f701a3de50' /></div>
  <div class="field-group">
    <label for="id_permission">Access</label>
    <select id="id_permission" name="permission"
            class="nosearch select">
    
      <option value="write">Write</option>
      <option value="admin">Admin</option>
    </select>
  </div>
</form>

          </li>
          
        </ul>
      </div>
      <div id="repo-toolbar" class="bb-toolbar">
        
        <div class="aui-buttons">
          <a id="repo-clone-button" class="aui-button aui-style" href="https://artscoop@bitbucket.org/artscoop/django-admin-autocomplete">
            <span class="icon clone">Clone Icon</span>
            <span>Clone</span>
            <span class="aui-icon-dropdown"></span>
          </a>
          <a id="fork-button" class="aui-button aui-style"
             href="/artscoop/django-admin-autocomplete/fork">
            <span class="icon fork">Fork Icon</span>
            <span>Fork</span>
          </a>
        </div>
        <div class="aui-buttons">
          <a id="compare-button" class="aui-button aui-style"
             href="/artscoop/django-admin-autocomplete/compare">
            <span class="icon compare">Compare Icon</span>
            <span>Compare</span>
          </a>
          <a id="pull-request-button" class="aui-button aui-style"
             href="/artscoop/django-admin-autocomplete/pull-request/new">
            <span class="icon pull-request">Pull Request Icon</span>
            <span>Pull Request</span>
          </a>
        </div>
        
        

<div id="repo-clone-dialog" class="clone-dialog hidden">
  
<div class="clone-url">
  <div class="aui-buttons">
    <a href="https://artscoop@bitbucket.org/artscoop/django-admin-autocomplete"
       class="aui-button aui-style aui-dropdown2-trigger" aria-haspopup="true"
       aria-owns="clone-url-dropdown-header">
      <span class="dropdown-text">HTTPS</span>
    </a>
    <div id="clone-url-dropdown-header" class="aui-dropdown2 aui-style-default">
      <ul class="aui-list-truncate">
        <li>
          <a href="https://artscoop@bitbucket.org/artscoop/django-admin-autocomplete"
            
              data-command="hg clone https://artscoop@bitbucket.org/artscoop/django-admin-autocomplete"
            
            class="item-link https">HTTPS
          </a>
        </li>
        <li>
          <a href="ssh://hg@bitbucket.org/artscoop/django-admin-autocomplete"
            
              data-command="hg clone ssh://hg@bitbucket.org/artscoop/django-admin-autocomplete"
            
            class="item-link ssh">SSH
          </a>
        </li>
      </ul>
    </div>
    <input type="text" readonly="readonly" value="hg clone https://artscoop@bitbucket.org/artscoop/django-admin-autocomplete">
  </div>
  
  <p>Need help cloning? Visit
     <a href="https://confluence.atlassian.com/x/cgozDQ" target="_blank">Bitbucket 101</a>.</p>
  
</div>

  
  
  <div class="clone-in-sourcetree"
       data-https-url="https://artscoop@bitbucket.org/artscoop/django-admin-autocomplete"
       data-ssh-url="ssh://hg@bitbucket.org/artscoop/django-admin-autocomplete">
    <p><button class="aui-button aui-style aui-button-primary">Clone in SourceTree</button></p>

    <p><a href="http://www.sourcetreeapp.com" target="_blank">SourceTree</a>
       is a free Mac client by Atlassian for Git, Mercurial and Subversion.</p>
  </div>
  
</div>

      </div>
    </div>
    <div class="clearfix"></div>
  </header>
  <nav id="repo-tabs" class="aui-navbar aui-navbar-roomy">
    <div class="aui-navbar-inner">
      <ul class="aui-nav aui-nav-horizontal">
        
          <li>
            <a href="/artscoop/django-admin-autocomplete/overview" id="repo-overview-link">Overview</a>
          </li>
        
        
          <li class="aui-nav-selected">
            <a href="/artscoop/django-admin-autocomplete/src" id="repo-source-link">Source</a>
          </li>
        
        
          <li>
            <a href="/artscoop/django-admin-autocomplete/changesets" id="repo-commits-link">
              Commits
            </a>
          </li>
        
        
          <li>
            <a href="/artscoop/django-admin-autocomplete/pull-requests" id="repo-pullrequests-link">
              Pull Requests
              
                
              
            </a>
          </li>
        
          <li id="issues-tab" class="
            
              
            
          ">
            <a href="/artscoop/django-admin-autocomplete/issues?status=new&amp;status=open" id="repo-issues-link">
              Issues
              
                
              
            </a>
          </li>
          <li id="wiki-tab" class="
              
                
              
            ">
            <a href="/artscoop/django-admin-autocomplete/wiki" id="repo-wiki-link">Wiki</a>
          </li>
        
          <li>
          <a href="/artscoop/django-admin-autocomplete/downloads" id="repo-downloads-link">
            Downloads
            
              
            
          </a>
          </li>
        
        
          <li id="admin-tab">
            <a href="/artscoop/django-admin-autocomplete/admin" id="repo-admin-link">
                <span class="icon settings">Administration</span>
            </a>
          </li>
        
      </ul>
    </div>
  </nav>

    <div id="content" role="main">
      
  <div id="repo-content">
    
  <div id="source-container">
    



<header id="source-path">
  
  <div class="labels labels-csv">
    
      <div class="aui-buttons">
        <button data-branches-tags-url="/api/1.0/repositories/artscoop/django-admin-autocomplete/branches-tags"
                class="aui-button aui-style branch-dialog-trigger" title="default">
          
            
              <span class="branch icon">Branch</span>
            
            <span class="name">default</span>
          
          <span class="aui-icon-dropdown"></span>
        </button>
      </div>
    
  </div>
  
  
    <div class="view-switcher">
      <div class="aui-buttons">
        
          <a href="/artscoop/django-admin-autocomplete/src/b26a9604d642/admin_autocomplete_mixin.py?at=default"
             class="aui-button aui-style pjax-trigger active">
            Source
          </a>
          <a href="/artscoop/django-admin-autocomplete/diff/admin_autocomplete_mixin.py?diff2=b26a9604d642&at=default"
             class="aui-button aui-style pjax-trigger "
             title="Diff to previous change">
            Diff
          </a>
          <a href="/artscoop/django-admin-autocomplete/history-node/b26a9604d642/admin_autocomplete_mixin.py?at=default"
             class="aui-button aui-style pjax-trigger ">
            History
          </a>
        
      </div>
    </div>
  
  <h1>
    <a href="/artscoop/django-admin-autocomplete/src/b26a9604d642?at=default"
       class="pjax-trigger" title="[u&#39;admin_autocomplete_mixin.py&#39;]">django-admin-autocomplete</a> /
    
      
        
          <span>admin_autocomplete_mixin.py</span>
        
      
    
  </h1>
  
    
    
  
  <div class="clearfix"></div>
</header>


  
    <div id="source-view">
      <div class="toolbar">
        <div class="primary">
          <div class="aui-buttons">
            
              <button id="file-history-trigger" class="aui-button aui-style changeset-info"
                      data-changeset="b26a9604d6429037f8b9b95906bb607ac6fe7951"
                      data-path="admin_autocomplete_mixin.py"
                      data-current="b26a9604d6429037f8b9b95906bb607ac6fe7951">
                
                   

<img class="avatar avatar16" src="https://secure.gravatar.com/avatar/91bbfb07eb02cd65caa550e7c468f832?d=https%3A%2F%2Fdwz7u9t8u8usb.cloudfront.net%2Fm%2Fa1fb05d05bb7%2Fimg%2Fdefault_avatar%2F16%2Fuser_blue.png&amp;s=16" alt="Rafael Belliard avatar" />
<span class="changeset-hash">b26a960</span>
<time datetime="2012-09-30T17:48:57+00:00" class="timestamp"></time>
<span class="aui-icon-dropdown"></span>

                
              </button>
            
          </div>
        </div>
          <div class="secondary">
            
              <div class="aui-buttons">
                <a href="/artscoop/django-admin-autocomplete/annotate/b26a9604d6429037f8b9b95906bb607ac6fe7951/admin_autocomplete_mixin.py?at=default"
                   class="aui-button aui-style pjax-trigger">Blame</a>
              </div>
            
            <div class="aui-buttons">
              
              <a href="/artscoop/django-admin-autocomplete/full-commit/b26a9604d642/admin_autocomplete_mixin.py" class="aui-button aui-style"
                 title="View full commit b26a960">Full Commit</a>
              
                <a id="embed-link" href="/artscoop/django-admin-autocomplete/src/b26a9604d6429037f8b9b95906bb607ac6fe7951/admin_autocomplete_mixin.py?embed=t"
                   class="aui-button aui-style">Embed</a>
              
              <a href="/artscoop/django-admin-autocomplete/raw/b26a9604d6429037f8b9b95906bb607ac6fe7951/admin_autocomplete_mixin.py"
                 class="aui-button aui-style">Raw</a>
            </div>
          </div>
        <div class="clearfix"></div>
      </div>
    </div>

    
      
        
          <div class="file-source">
            <table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#cl-1">  1</a>
<a href="#cl-2">  2</a>
<a href="#cl-3">  3</a>
<a href="#cl-4">  4</a>
<a href="#cl-5">  5</a>
<a href="#cl-6">  6</a>
<a href="#cl-7">  7</a>
<a href="#cl-8">  8</a>
<a href="#cl-9">  9</a>
<a href="#cl-10"> 10</a>
<a href="#cl-11"> 11</a>
<a href="#cl-12"> 12</a>
<a href="#cl-13"> 13</a>
<a href="#cl-14"> 14</a>
<a href="#cl-15"> 15</a>
<a href="#cl-16"> 16</a>
<a href="#cl-17"> 17</a>
<a href="#cl-18"> 18</a>
<a href="#cl-19"> 19</a>
<a href="#cl-20"> 20</a>
<a href="#cl-21"> 21</a>
<a href="#cl-22"> 22</a>
<a href="#cl-23"> 23</a>
<a href="#cl-24"> 24</a>
<a href="#cl-25"> 25</a>
<a href="#cl-26"> 26</a>
<a href="#cl-27"> 27</a>
<a href="#cl-28"> 28</a>
<a href="#cl-29"> 29</a>
<a href="#cl-30"> 30</a>
<a href="#cl-31"> 31</a>
<a href="#cl-32"> 32</a>
<a href="#cl-33"> 33</a>
<a href="#cl-34"> 34</a>
<a href="#cl-35"> 35</a>
<a href="#cl-36"> 36</a>
<a href="#cl-37"> 37</a>
<a href="#cl-38"> 38</a>
<a href="#cl-39"> 39</a>
<a href="#cl-40"> 40</a>
<a href="#cl-41"> 41</a>
<a href="#cl-42"> 42</a>
<a href="#cl-43"> 43</a>
<a href="#cl-44"> 44</a>
<a href="#cl-45"> 45</a>
<a href="#cl-46"> 46</a>
<a href="#cl-47"> 47</a>
<a href="#cl-48"> 48</a>
<a href="#cl-49"> 49</a>
<a href="#cl-50"> 50</a>
<a href="#cl-51"> 51</a>
<a href="#cl-52"> 52</a>
<a href="#cl-53"> 53</a>
<a href="#cl-54"> 54</a>
<a href="#cl-55"> 55</a>
<a href="#cl-56"> 56</a>
<a href="#cl-57"> 57</a>
<a href="#cl-58"> 58</a>
<a href="#cl-59"> 59</a>
<a href="#cl-60"> 60</a>
<a href="#cl-61"> 61</a>
<a href="#cl-62"> 62</a>
<a href="#cl-63"> 63</a>
<a href="#cl-64"> 64</a>
<a href="#cl-65"> 65</a>
<a href="#cl-66"> 66</a>
<a href="#cl-67"> 67</a>
<a href="#cl-68"> 68</a>
<a href="#cl-69"> 69</a>
<a href="#cl-70"> 70</a>
<a href="#cl-71"> 71</a>
<a href="#cl-72"> 72</a>
<a href="#cl-73"> 73</a>
<a href="#cl-74"> 74</a>
<a href="#cl-75"> 75</a>
<a href="#cl-76"> 76</a>
<a href="#cl-77"> 77</a>
<a href="#cl-78"> 78</a>
<a href="#cl-79"> 79</a>
<a href="#cl-80"> 80</a>
<a href="#cl-81"> 81</a>
<a href="#cl-82"> 82</a>
<a href="#cl-83"> 83</a>
<a href="#cl-84"> 84</a>
<a href="#cl-85"> 85</a>
<a href="#cl-86"> 86</a>
<a href="#cl-87"> 87</a>
<a href="#cl-88"> 88</a>
<a href="#cl-89"> 89</a>
<a href="#cl-90"> 90</a>
<a href="#cl-91"> 91</a>
<a href="#cl-92"> 92</a>
<a href="#cl-93"> 93</a>
<a href="#cl-94"> 94</a>
<a href="#cl-95"> 95</a>
<a href="#cl-96"> 96</a>
<a href="#cl-97"> 97</a>
<a href="#cl-98"> 98</a>
<a href="#cl-99"> 99</a>
<a href="#cl-100">100</a>
<a href="#cl-101">101</a>
<a href="#cl-102">102</a>
<a href="#cl-103">103</a>
<a href="#cl-104">104</a>
<a href="#cl-105">105</a>
<a href="#cl-106">106</a>
<a href="#cl-107">107</a>
<a href="#cl-108">108</a>
<a href="#cl-109">109</a>
<a href="#cl-110">110</a>
<a href="#cl-111">111</a>
<a href="#cl-112">112</a>
<a href="#cl-113">113</a>
<a href="#cl-114">114</a>
<a href="#cl-115">115</a>
<a href="#cl-116">116</a>
<a href="#cl-117">117</a>
<a href="#cl-118">118</a>
<a href="#cl-119">119</a>
<a href="#cl-120">120</a>
<a href="#cl-121">121</a>
<a href="#cl-122">122</a>
<a href="#cl-123">123</a>
<a href="#cl-124">124</a>
<a href="#cl-125">125</a>
<a href="#cl-126">126</a>
<a href="#cl-127">127</a>
<a href="#cl-128">128</a>
<a href="#cl-129">129</a>
<a href="#cl-130">130</a>
<a href="#cl-131">131</a>
<a href="#cl-132">132</a>
<a href="#cl-133">133</a>
<a href="#cl-134">134</a>
<a href="#cl-135">135</a>
<a href="#cl-136">136</a>
<a href="#cl-137">137</a>
<a href="#cl-138">138</a>
<a href="#cl-139">139</a>
<a href="#cl-140">140</a>
<a href="#cl-141">141</a>
<a href="#cl-142">142</a>
<a href="#cl-143">143</a>
<a href="#cl-144">144</a>
<a href="#cl-145">145</a>
<a href="#cl-146">146</a>
<a href="#cl-147">147</a>
<a href="#cl-148">148</a>
<a href="#cl-149">149</a>
<a href="#cl-150">150</a>
<a href="#cl-151">151</a>
<a href="#cl-152">152</a>
<a href="#cl-153">153</a>
<a href="#cl-154">154</a>
<a href="#cl-155">155</a>
<a href="#cl-156">156</a>
<a href="#cl-157">157</a>
<a href="#cl-158">158</a>
<a href="#cl-159">159</a>
<a href="#cl-160">160</a>
<a href="#cl-161">161</a>
<a href="#cl-162">162</a>
<a href="#cl-163">163</a>
<a href="#cl-164">164</a>
<a href="#cl-165">165</a>
<a href="#cl-166">166</a>
<a href="#cl-167">167</a>
<a href="#cl-168">168</a>
<a href="#cl-169">169</a>
<a href="#cl-170">170</a>
<a href="#cl-171">171</a>
<a href="#cl-172">172</a>
<a href="#cl-173">173</a>
<a href="#cl-174">174</a>
<a href="#cl-175">175</a>
<a href="#cl-176">176</a>
<a href="#cl-177">177</a>
<a href="#cl-178">178</a>
<a href="#cl-179">179</a>
<a href="#cl-180">180</a>
<a href="#cl-181">181</a>
<a href="#cl-182">182</a>
<a href="#cl-183">183</a>
<a href="#cl-184">184</a>
<a href="#cl-185">185</a>
<a href="#cl-186">186</a>
<a href="#cl-187">187</a>
<a href="#cl-188">188</a>
<a href="#cl-189">189</a>
<a href="#cl-190">190</a>
<a href="#cl-191">191</a>
<a href="#cl-192">192</a>
<a href="#cl-193">193</a>
<a href="#cl-194">194</a>
<a href="#cl-195">195</a>
<a href="#cl-196">196</a>
<a href="#cl-197">197</a>
<a href="#cl-198">198</a>
<a href="#cl-199">199</a>
<a href="#cl-200">200</a>
<a href="#cl-201">201</a>
<a href="#cl-202">202</a>
<a href="#cl-203">203</a>
<a href="#cl-204">204</a>
<a href="#cl-205">205</a>
<a href="#cl-206">206</a>
<a href="#cl-207">207</a>
<a href="#cl-208">208</a>
<a href="#cl-209">209</a>
<a href="#cl-210">210</a>
<a href="#cl-211">211</a>
<a href="#cl-212">212</a>
<a href="#cl-213">213</a>
<a href="#cl-214">214</a>
<a href="#cl-215">215</a>
<a href="#cl-216">216</a>
<a href="#cl-217">217</a>
<a href="#cl-218">218</a>
<a href="#cl-219">219</a>
<a href="#cl-220">220</a>
<a href="#cl-221">221</a>
<a href="#cl-222">222</a>
<a href="#cl-223">223</a>
<a href="#cl-224">224</a>
<a href="#cl-225">225</a>
<a href="#cl-226">226</a>
<a href="#cl-227">227</a>
<a href="#cl-228">228</a>
<a href="#cl-229">229</a>
<a href="#cl-230">230</a>
<a href="#cl-231">231</a>
<a href="#cl-232">232</a></pre></div></td><td class="code"><div class="highlight"><pre><a name="cl-1"></a><span class="c"># for autocomplete</span>
<a name="cl-2"></a><span class="kn">import</span> <span class="nn">operator</span>
<a name="cl-3"></a>
<a name="cl-4"></a><span class="kn">from</span> <span class="nn">django</span> <span class="kn">import</span> <span class="n">forms</span>
<a name="cl-5"></a><span class="kn">from</span> <span class="nn">django.db</span> <span class="kn">import</span> <span class="n">models</span>
<a name="cl-6"></a><span class="kn">from</span> <span class="nn">django.utils.encoding</span> <span class="kn">import</span> <span class="n">smart_str</span>
<a name="cl-7"></a><span class="kn">from</span> <span class="nn">django.utils.safestring</span> <span class="kn">import</span> <span class="n">mark_safe</span>
<a name="cl-8"></a><span class="kn">from</span> <span class="nn">django.conf.urls.defaults</span> <span class="kn">import</span> <span class="n">patterns</span>
<a name="cl-9"></a><span class="kn">from</span> <span class="nn">django.db.models.query</span> <span class="kn">import</span> <span class="n">QuerySet</span>
<a name="cl-10"></a><span class="kn">from</span> <span class="nn">django.http</span> <span class="kn">import</span> <span class="n">HttpResponse</span><span class="p">,</span> <span class="n">HttpResponseNotFound</span>
<a name="cl-11"></a><span class="kn">from</span> <span class="nn">django.conf</span> <span class="kn">import</span> <span class="n">settings</span>
<a name="cl-12"></a>
<a name="cl-13"></a><span class="c"># based and inspired by http://jannisleidel.com/2008/11/autocomplete-form-widget-foreignkey-model-fields/</span>
<a name="cl-14"></a><span class="k">class</span> <span class="nc">AutocompleteFKMixin</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-15"></a>    <span class="k">def</span> <span class="nf">get_urls</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-16"></a>        <span class="n">urls</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">AutocompleteFKMixin</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">get_urls</span><span class="p">()</span>
<a name="cl-17"></a>        <span class="n">search_url</span> <span class="o">=</span> <span class="n">patterns</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">,</span>
<a name="cl-18"></a>            <span class="p">(</span><span class="s">r&#39;^search/$&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">search</span><span class="p">)</span>
<a name="cl-19"></a>        <span class="p">)</span>
<a name="cl-20"></a>        <span class="k">return</span> <span class="n">search_url</span> <span class="o">+</span> <span class="n">urls</span>
<a name="cl-21"></a>
<a name="cl-22"></a>    <span class="k">def</span> <span class="nf">get_autocomplete_queryset</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">field_name</span><span class="p">):</span>
<a name="cl-23"></a>        <span class="sd">&quot;&quot;&quot;</span>
<a name="cl-24"></a><span class="sd">        Returns the basic queryset to filter results for an autocomplete field `field_name`.</span>
<a name="cl-25"></a><span class="sd">        If None is returned - all db objects are used for a queryset.</span>
<a name="cl-26"></a><span class="sd">        &quot;&quot;&quot;</span>
<a name="cl-27"></a>        <span class="k">return</span> <span class="bp">None</span>
<a name="cl-28"></a>
<a name="cl-29"></a>    <span class="k">def</span> <span class="nf">search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">):</span>
<a name="cl-30"></a>        <span class="sd">&quot;&quot;&quot;</span>
<a name="cl-31"></a><span class="sd">        Searches in the fields of the given related model and returns the</span>
<a name="cl-32"></a><span class="sd">        result as a simple string to be used by the jQuery Autocomplete plugin</span>
<a name="cl-33"></a><span class="sd">        &quot;&quot;&quot;</span>
<a name="cl-34"></a>        <span class="n">query</span>         <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">GET</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;q&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span>
<a name="cl-35"></a>        <span class="n">app_label</span>     <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">GET</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;app_label&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span>
<a name="cl-36"></a>        <span class="n">model_name</span>    <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">GET</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;model_name&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span>
<a name="cl-37"></a>        <span class="n">search_fields</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">GET</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;search_fields&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span>
<a name="cl-38"></a>        <span class="n">field_name</span>    <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">GET</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;field_name&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span>
<a name="cl-39"></a>        <span class="n">related_fields</span> <span class="o">=</span> <span class="p">[</span><span class="n">field</span><span class="p">[:</span><span class="o">-</span><span class="mi">3</span><span class="p">]</span> <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">request</span><span class="o">.</span><span class="n">GET</span>
<a name="cl-40"></a>            <span class="k">if</span> <span class="n">field</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">:]</span> <span class="o">==</span> <span class="s">&quot;_pk&quot;</span> <span class="ow">and</span> <span class="n">request</span><span class="o">.</span><span class="n">GET</span><span class="p">[</span><span class="n">field</span><span class="p">]]</span>
<a name="cl-41"></a>
<a name="cl-42"></a>        <span class="c"># remove all garbage and injections</span>
<a name="cl-43"></a>        <span class="kn">from</span> <span class="nn">django.template.defaultfilters</span> <span class="kn">import</span> <span class="n">slugify</span>
<a name="cl-44"></a>        <span class="n">search_fields</span> <span class="o">=</span> <span class="p">[</span><span class="n">f</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">search_fields</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;,&#39;</span><span class="p">)</span> <span class="k">if</span> <span class="n">f</span><span class="o">==</span><span class="n">slugify</span><span class="p">(</span><span class="n">f</span><span class="p">)]</span>
<a name="cl-45"></a>
<a name="cl-46"></a>        <span class="k">if</span> <span class="n">search_fields</span> <span class="ow">and</span> <span class="n">app_label</span> <span class="ow">and</span> <span class="n">model_name</span> <span class="ow">and</span> <span class="n">query</span><span class="p">:</span>
<a name="cl-47"></a>            <span class="k">def</span> <span class="nf">construct_search</span><span class="p">(</span><span class="n">field_name</span><span class="p">):</span>
<a name="cl-48"></a>                <span class="c"># use different lookup methods depending on the notation</span>
<a name="cl-49"></a>                <span class="k">if</span> <span class="n">field_name</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;^&#39;</span><span class="p">):</span>
<a name="cl-50"></a>                    <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">__istartswith&quot;</span> <span class="o">%</span> <span class="n">field_name</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
<a name="cl-51"></a>                <span class="k">elif</span> <span class="n">field_name</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">):</span>
<a name="cl-52"></a>                    <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">__iexact&quot;</span> <span class="o">%</span> <span class="n">field_name</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
<a name="cl-53"></a>                <span class="k">elif</span> <span class="n">field_name</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;@&#39;</span><span class="p">):</span>
<a name="cl-54"></a>                    <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">__search&quot;</span> <span class="o">%</span> <span class="n">field_name</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
<a name="cl-55"></a>                <span class="k">else</span><span class="p">:</span>
<a name="cl-56"></a>                    <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">__icontains&quot;</span> <span class="o">%</span> <span class="n">field_name</span>
<a name="cl-57"></a>
<a name="cl-58"></a>            <span class="n">model</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">get_model</span><span class="p">(</span><span class="n">app_label</span><span class="p">,</span> <span class="n">model_name</span><span class="p">)</span>
<a name="cl-59"></a>            <span class="n">qs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_autocomplete_queryset</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">field_name</span><span class="p">)</span>
<a name="cl-60"></a>            <span class="k">if</span> <span class="n">qs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-61"></a>                <span class="n">qs</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">_default_manager</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
<a name="cl-62"></a>            <span class="k">for</span> <span class="n">bit</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">split</span><span class="p">():</span>
<a name="cl-63"></a>                <span class="n">or_queries</span> <span class="o">=</span> <span class="p">[</span><span class="n">models</span><span class="o">.</span><span class="n">Q</span><span class="p">(</span><span class="o">**</span><span class="p">{</span><span class="n">construct_search</span><span class="p">(</span>
<a name="cl-64"></a>                    <span class="n">smart_str</span><span class="p">(</span><span class="n">field_name</span><span class="p">)):</span> <span class="n">smart_str</span><span class="p">(</span><span class="n">bit</span><span class="p">)})</span>
<a name="cl-65"></a>                        <span class="k">for</span> <span class="n">field_name</span> <span class="ow">in</span> <span class="n">search_fields</span><span class="p">]</span>
<a name="cl-66"></a>
<a name="cl-67"></a>                <span class="n">other_qs</span> <span class="o">=</span> <span class="n">QuerySet</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<a name="cl-68"></a>                <span class="n">other_qs</span><span class="o">.</span><span class="n">dup_select_related</span><span class="p">(</span><span class="n">qs</span><span class="p">)</span>
<a name="cl-69"></a>                <span class="n">other_qs</span> <span class="o">=</span> <span class="n">other_qs</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="nb">reduce</span><span class="p">(</span><span class="n">operator</span><span class="o">.</span><span class="n">or_</span><span class="p">,</span> <span class="n">or_queries</span><span class="p">))</span>
<a name="cl-70"></a>                <span class="n">qs</span> <span class="o">=</span> <span class="n">qs</span> <span class="o">&amp;</span> <span class="n">other_qs</span>
<a name="cl-71"></a>            <span class="c"># filter out by related ids</span>
<a name="cl-72"></a>            <span class="n">qs</span> <span class="o">=</span> <span class="n">qs</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="o">**</span><span class="nb">dict</span><span class="p">([(</span><span class="nb">str</span><span class="p">(</span><span class="n">field</span><span class="p">),</span> <span class="n">request</span><span class="o">.</span><span class="n">GET</span><span class="p">[</span><span class="n">field</span><span class="o">+</span><span class="s">&quot;_pk&quot;</span><span class="p">])</span> <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">related_fields</span><span class="p">]))</span>
<a name="cl-73"></a>            <span class="c"># sort rows directly containing query be the first</span>
<a name="cl-74"></a>            <span class="kn">from</span> <span class="nn">django.utils.datastructures</span> <span class="kn">import</span> <span class="n">SortedDict</span>
<a name="cl-75"></a>
<a name="cl-76"></a>            <span class="c"># we do not was to dig into __ relations here. Only first model fields go for smart sorting.</span>
<a name="cl-77"></a>            <span class="n">smartsorted_fields</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-78"></a>            <span class="k">for</span> <span class="n">field_name</span> <span class="ow">in</span> <span class="n">search_fields</span><span class="p">:</span>
<a name="cl-79"></a>                <span class="c"># add qualifying table</span>
<a name="cl-80"></a>                <span class="k">try</span><span class="p">:</span>
<a name="cl-81"></a>                    <span class="n">model</span><span class="o">.</span><span class="n">_meta</span><span class="o">.</span><span class="n">get_field_by_name</span><span class="p">(</span><span class="n">field_name</span><span class="p">)</span>
<a name="cl-82"></a>                <span class="k">except</span><span class="p">:</span>
<a name="cl-83"></a>                    <span class="k">continue</span>
<a name="cl-84"></a>                <span class="n">smartsorted_fields</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">field_name</span><span class="p">)</span>
<a name="cl-85"></a>
<a name="cl-86"></a>            <span class="k">for</span> <span class="n">field_name</span> <span class="ow">in</span> <span class="n">smartsorted_fields</span><span class="p">:</span>
<a name="cl-87"></a>                <span class="n">full_field_name</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">_meta</span><span class="o">.</span><span class="n">db_table</span><span class="o">+</span><span class="s">&quot;.&quot;</span><span class="o">+</span><span class="n">field_name</span>
<a name="cl-88"></a>                <span class="n">qs</span> <span class="o">=</span> <span class="n">qs</span><span class="o">.</span><span class="n">extra</span><span class="p">(</span><span class="n">select</span><span class="o">=</span><span class="n">SortedDict</span><span class="p">([</span>
<a name="cl-89"></a>                    <span class="p">(</span><span class="s">&#39;_</span><span class="si">%s</span><span class="s">_match&#39;</span> <span class="o">%</span> <span class="n">field_name</span><span class="p">,</span>
<a name="cl-90"></a>                        <span class="s">&quot;CASE WHEN lower(&quot;</span><span class="o">+</span><span class="n">full_field_name</span><span class="o">+</span><span class="s">&quot;)=lower(</span><span class="si">%s</span><span class="s">) THEN 1 ELSE 0 END&quot;</span><span class="p">),</span>
<a name="cl-91"></a>                    <span class="p">(</span><span class="s">&#39;_</span><span class="si">%s</span><span class="s">_contains&#39;</span> <span class="o">%</span> <span class="n">field_name</span><span class="p">,</span>
<a name="cl-92"></a>                    <span class="c"># can not put percents here because of http://code.djangoproject.com/ticket/6400</span>
<a name="cl-93"></a>                        <span class="s">&quot;CASE WHEN &quot;</span><span class="o">+</span><span class="n">full_field_name</span><span class="o">+</span><span class="s">&quot; LIKE </span><span class="si">%s</span><span class="s"> THEN 1 ELSE 0 END&quot;</span><span class="p">),</span>
<a name="cl-94"></a>                    <span class="p">]),</span> <span class="n">select_params</span> <span class="o">=</span> <span class="p">[</span><span class="n">query</span><span class="p">,</span> <span class="s">&#39;%&#39;</span><span class="o">+</span><span class="n">query</span><span class="o">+</span><span class="s">&#39;%&#39;</span><span class="p">])</span>
<a name="cl-95"></a>            <span class="n">ordering</span> <span class="o">=</span> <span class="p">[</span> <span class="p">[</span><span class="s">&#39;-_</span><span class="si">%s</span><span class="s">_match&#39;</span> <span class="o">%</span> <span class="n">field_name</span><span class="p">,</span> <span class="s">&#39;-_</span><span class="si">%s</span><span class="s">_contains&#39;</span> <span class="o">%</span> <span class="n">field_name</span><span class="p">]</span>
<a name="cl-96"></a>                <span class="k">for</span> <span class="n">field_name</span> <span class="ow">in</span> <span class="n">smartsorted_fields</span><span class="p">]</span>
<a name="cl-97"></a>            <span class="c"># flatten list of sorting options</span>
<a name="cl-98"></a>            <span class="n">ordering</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">ordering</span><span class="p">,</span> <span class="p">[])</span>
<a name="cl-99"></a>            <span class="n">qs</span> <span class="o">=</span> <span class="n">qs</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="o">*</span><span class="n">ordering</span><span class="p">)</span>
<a name="cl-100"></a>            <span class="n">qs</span> <span class="o">=</span> <span class="n">qs</span><span class="p">[:</span><span class="mi">25</span><span class="p">]</span>
<a name="cl-101"></a>
<a name="cl-102"></a>            <span class="c"># sometimes we want to present suggestions in a special way</span>
<a name="cl-103"></a>            <span class="k">def</span> <span class="nf">ajax_str</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
<a name="cl-104"></a>                <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="s">&#39;ajax_str&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">callable</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">ajax_str</span><span class="p">):</span>
<a name="cl-105"></a>                    <span class="k">return</span> <span class="n">obj</span><span class="o">.</span><span class="n">ajax_str</span><span class="p">()</span>
<a name="cl-106"></a>                <span class="k">else</span><span class="p">:</span>
<a name="cl-107"></a>                    <span class="k">return</span> <span class="nb">unicode</span><span class="p">(</span><span class="nb">object</span><span class="p">)</span>
<a name="cl-108"></a>
<a name="cl-109"></a>            <span class="n">data</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s">u&#39;</span><span class="si">%s</span><span class="s">|</span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">ajax_str</span><span class="p">(</span><span class="n">f</span><span class="p">),</span> <span class="n">f</span><span class="o">.</span><span class="n">pk</span><span class="p">)</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">qs</span><span class="p">])</span>
<a name="cl-110"></a>            <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">mimetype</span><span class="o">=</span><span class="s">&#39;text/plain&#39;</span><span class="p">)</span>
<a name="cl-111"></a>        <span class="k">return</span> <span class="n">HttpResponseNotFound</span><span class="p">()</span>
<a name="cl-112"></a>
<a name="cl-113"></a>    <span class="k">def</span> <span class="nf">formfield_for_dbfield</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_field</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
<a name="cl-114"></a>        <span class="sd">&quot;&quot;&quot;</span>
<a name="cl-115"></a><span class="sd">        Overrides the default widget for Foreignkey fields if they are</span>
<a name="cl-116"></a><span class="sd">        specified in the related_search_fields class attribute.</span>
<a name="cl-117"></a><span class="sd">        &quot;&quot;&quot;</span>
<a name="cl-118"></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">db_field</span><span class="p">,</span> <span class="n">models</span><span class="o">.</span><span class="n">ForeignKey</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&#39;related_search_fields&#39;</span><span class="p">)</span> \
<a name="cl-119"></a>                <span class="ow">and</span> <span class="n">db_field</span><span class="o">.</span><span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">related_search_fields</span><span class="p">:</span>
<a name="cl-120"></a>            <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;widget&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">ForeignKeySearchInput</span><span class="p">(</span><span class="n">db_field</span><span class="o">.</span><span class="n">rel</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">related_search_fields</span><span class="p">[</span><span class="n">db_field</span><span class="o">.</span><span class="n">name</span><span class="p">])</span>
<a name="cl-121"></a>        <span class="k">return</span> <span class="nb">super</span><span class="p">(</span><span class="n">AutocompleteFKMixin</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">formfield_for_dbfield</span><span class="p">(</span><span class="n">db_field</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
<a name="cl-122"></a>
<a name="cl-123"></a>
<a name="cl-124"></a><span class="k">class</span> <span class="nc">ForeignKeySearchInput</span><span class="p">(</span><span class="n">forms</span><span class="o">.</span><span class="n">TextInput</span><span class="p">):</span>
<a name="cl-125"></a>    <span class="sd">&quot;&quot;&quot;</span>
<a name="cl-126"></a><span class="sd">    A Widget for displaying ForeignKeys in an autocomplete search input</span>
<a name="cl-127"></a><span class="sd">    instead in a ``select`` box.</span>
<a name="cl-128"></a><span class="sd">    &quot;&quot;&quot;</span>
<a name="cl-129"></a>    <span class="k">class</span> <span class="nc">Media</span><span class="p">:</span>
<a name="cl-130"></a>        <span class="n">css</span> <span class="o">=</span> <span class="p">{</span>
<a name="cl-131"></a>            <span class="s">&#39;all&#39;</span><span class="p">:</span> <span class="p">(</span><span class="s">&#39;js/autocomplete/jquery.autocomplete.css&#39;</span><span class="p">,)</span>
<a name="cl-132"></a>        <span class="p">}</span>
<a name="cl-133"></a>        <span class="n">js</span> <span class="o">=</span> <span class="p">(</span>
<a name="cl-134"></a>            <span class="c"># Breaks our current &lt;script&gt; order. See GoodBed Trac #1061.</span>
<a name="cl-135"></a>            <span class="c"># &#39;js/jquery.min.js&#39;,</span>
<a name="cl-136"></a>            <span class="s">&#39;js/autocomplete/jquery.autocomplete.js&#39;</span><span class="p">,</span>
<a name="cl-137"></a>        <span class="p">)</span>
<a name="cl-138"></a>    <span class="n">input_type</span> <span class="o">=</span> <span class="s">&#39;hidden&#39;</span>
<a name="cl-139"></a>
<a name="cl-140"></a>    <span class="k">def</span> <span class="nf">label_for_value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
<a name="cl-141"></a>        <span class="kn">from</span> <span class="nn">django.utils.text</span> <span class="kn">import</span> <span class="n">truncate_words</span>
<a name="cl-142"></a>        <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rel</span><span class="o">.</span><span class="n">get_related_field</span><span class="p">()</span><span class="o">.</span><span class="n">name</span>
<a name="cl-143"></a>        <span class="n">obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rel</span><span class="o">.</span><span class="n">to</span><span class="o">.</span><span class="n">_default_manager</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="o">**</span><span class="p">{</span><span class="n">key</span><span class="p">:</span> <span class="n">value</span><span class="p">})</span>
<a name="cl-144"></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="s">&#39;ajax_str&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">callable</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">ajax_str</span><span class="p">):</span>
<a name="cl-145"></a>            <span class="n">obj</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">ajax_str</span><span class="p">()</span>
<a name="cl-146"></a>        <span class="k">return</span> <span class="n">truncate_words</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="mi">14</span><span class="p">)</span>
<a name="cl-147"></a>
<a name="cl-148"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="n">search_fields</span><span class="p">,</span> <span class="n">attrs</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-149"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">rel</span> <span class="o">=</span> <span class="n">rel</span>
<a name="cl-150"></a>
<a name="cl-151"></a>        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">search_fields</span><span class="p">)</span> <span class="o">==</span> <span class="nb">dict</span><span class="p">:</span>
<a name="cl-152"></a>            <span class="c"># fancy lookup for manufacturer_pk, like_pk etc</span>
<a name="cl-153"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">search_fields</span> <span class="o">=</span> <span class="n">search_fields</span><span class="p">[</span><span class="s">&#39;search&#39;</span><span class="p">]</span>
<a name="cl-154"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">related_fields</span> <span class="o">=</span> <span class="n">search_fields</span><span class="p">[</span><span class="s">&#39;related&#39;</span><span class="p">]</span>
<a name="cl-155"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-156"></a>            <span class="c"># plain string lookup</span>
<a name="cl-157"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">search_fields</span> <span class="o">=</span> <span class="n">search_fields</span>
<a name="cl-158"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">related_fields</span> <span class="o">=</span> <span class="bp">None</span>
<a name="cl-159"></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ForeignKeySearchInput</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="n">attrs</span><span class="p">)</span>
<a name="cl-160"></a>
<a name="cl-161"></a>    <span class="k">def</span> <span class="nf">render</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">attrs</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-162"></a>        <span class="k">if</span> <span class="n">attrs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-163"></a>            <span class="n">attrs</span> <span class="o">=</span> <span class="p">{}</span>
<a name="cl-164"></a>        <span class="n">rendered</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">ForeignKeySearchInput</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">attrs</span><span class="p">)</span>
<a name="cl-165"></a>        <span class="k">if</span> <span class="n">value</span><span class="p">:</span>
<a name="cl-166"></a>            <span class="n">label</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">label_for_value</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
<a name="cl-167"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-168"></a>            <span class="n">label</span> <span class="o">=</span> <span class="s">u&#39;&#39;</span>
<a name="cl-169"></a>
<a name="cl-170"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">related_fields</span><span class="p">:</span>
<a name="cl-171"></a>            <span class="n">extra_params</span> <span class="o">=</span> <span class="s">&#39;,&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span>
<a name="cl-172"></a>                <span class="s">&quot;</span><span class="si">%s</span><span class="s">_pk: function(){ return jQuery(&#39;#id_</span><span class="si">%s</span><span class="s">&#39;).val(); }&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">field</span><span class="p">,</span> <span class="n">field</span><span class="p">)</span>
<a name="cl-173"></a>                    <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">related_fields</span><span class="p">])</span>
<a name="cl-174"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-175"></a>            <span class="n">extra_params</span> <span class="o">=</span> <span class="s">&#39;&#39;</span>
<a name="cl-176"></a>
<a name="cl-177"></a>        <span class="c"># Play nice with Django 1.4</span>
<a name="cl-178"></a>        <span class="k">try</span><span class="p">:</span>
<a name="cl-179"></a>            <span class="n">admin_media_prefix</span> <span class="o">=</span> <span class="n">settings</span><span class="o">.</span><span class="n">ADMIN_MEDIA_PREFIX</span>
<a name="cl-180"></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
<a name="cl-181"></a>            <span class="n">admin_media_prefix</span> <span class="o">=</span> <span class="n">settings</span><span class="o">.</span><span class="n">STATIC_URL</span> <span class="o">+</span> <span class="s">&quot;admin/&quot;</span>
<a name="cl-182"></a>
<a name="cl-183"></a>        <span class="k">return</span> <span class="n">rendered</span> <span class="o">+</span> <span class="n">mark_safe</span><span class="p">(</span><span class="s">u&#39;&#39;&#39;</span>
<a name="cl-184"></a><span class="s">            &lt;style type=&quot;text/css&quot; media=&quot;screen&quot;&gt;</span>
<a name="cl-185"></a><span class="s">                #lookup_</span><span class="si">%(name)s</span><span class="s"> {</span>
<a name="cl-186"></a><span class="s">                    padding-right:16px;</span>
<a name="cl-187"></a><span class="s">                    background: url(</span>
<a name="cl-188"></a><span class="s">                        </span><span class="si">%(admin_media_prefix)s</span><span class="s">img/selector-search.gif</span>
<a name="cl-189"></a><span class="s">                    ) no-repeat right;</span>
<a name="cl-190"></a><span class="s">                }</span>
<a name="cl-191"></a><span class="s">                #del_</span><span class="si">%(name)s</span><span class="s"> {</span>
<a name="cl-192"></a><span class="s">                    display: none;</span>
<a name="cl-193"></a><span class="s">                }</span>
<a name="cl-194"></a><span class="s">            &lt;/style&gt;</span>
<a name="cl-195"></a><span class="s">&lt;input type=&quot;text&quot; id=&quot;lookup_</span><span class="si">%(name)s</span><span class="s">&quot; value=&quot;</span><span class="si">%(label)s</span><span class="s">&quot; /&gt;</span>
<a name="cl-196"></a><span class="s">&lt;a href=&quot;#&quot; id=&quot;del_</span><span class="si">%(name)s</span><span class="s">&quot;&gt;</span>
<a name="cl-197"></a><span class="s">&lt;img src=&quot;</span><span class="si">%(admin_media_prefix)s</span><span class="s">img/icon_deletelink.gif&quot; /&gt;</span>
<a name="cl-198"></a><span class="s">&lt;/a&gt;</span>
<a name="cl-199"></a><span class="s">&lt;script type=&quot;text/javascript&quot;&gt;</span>
<a name="cl-200"></a><span class="s">            if ($(&#39;#lookup_</span><span class="si">%(name)s</span><span class="s">&#39;).val()) {</span>
<a name="cl-201"></a><span class="s">                $(&#39;#del_</span><span class="si">%(name)s</span><span class="s">&#39;).show()</span>
<a name="cl-202"></a><span class="s">            }</span>
<a name="cl-203"></a><span class="s">            $(&#39;#lookup_</span><span class="si">%(name)s</span><span class="s">&#39;).autocomplete(&#39;../search/&#39;, {</span>
<a name="cl-204"></a><span class="s">                &#39;minChars&#39;: 1, &#39;cacheLength&#39;: 0, &#39;max&#39;:35,</span>
<a name="cl-205"></a><span class="s">                &#39;extraParams&#39;: {</span>
<a name="cl-206"></a><span class="s">                    search_fields: &#39;</span><span class="si">%(search_fields)s</span><span class="s">&#39;,</span>
<a name="cl-207"></a><span class="s">                    app_label: &#39;</span><span class="si">%(app_label)s</span><span class="s">&#39;,</span>
<a name="cl-208"></a><span class="s">                    model_name: &#39;</span><span class="si">%(model_name)s</span><span class="s">&#39;,</span>
<a name="cl-209"></a><span class="s">                    field_name: &#39;</span><span class="si">%(name)s</span><span class="s">&#39;,</span>
<a name="cl-210"></a><span class="s">                    </span><span class="si">%(extra_params)s</span><span class="s"></span>
<a name="cl-211"></a><span class="s">                },</span>
<a name="cl-212"></a><span class="s">            }).result(function(event, data, formatted) {</span>
<a name="cl-213"></a><span class="s">                if (data) {</span>
<a name="cl-214"></a><span class="s">                    $(&#39;#id_</span><span class="si">%(name)s</span><span class="s">&#39;).val(data[1]);</span>
<a name="cl-215"></a><span class="s">                    $(&#39;#del_</span><span class="si">%(name)s</span><span class="s">&#39;).show();</span>
<a name="cl-216"></a><span class="s">                }</span>
<a name="cl-217"></a><span class="s">            });</span>
<a name="cl-218"></a><span class="s">            $(&#39;#del_</span><span class="si">%(name)s</span><span class="s">&#39;).click(function(ele, event) {</span>
<a name="cl-219"></a><span class="s">                $(&#39;#id_</span><span class="si">%(name)s</span><span class="s">&#39;).val(&#39;&#39;);</span>
<a name="cl-220"></a><span class="s">                $(&#39;#del_</span><span class="si">%(name)s</span><span class="s">&#39;).hide();</span>
<a name="cl-221"></a><span class="s">                $(&#39;#lookup_</span><span class="si">%(name)s</span><span class="s">&#39;).val(&#39;&#39;);</span>
<a name="cl-222"></a><span class="s">            });</span>
<a name="cl-223"></a><span class="s">            &lt;/script&gt;</span>
<a name="cl-224"></a><span class="s">        &#39;&#39;&#39;</span><span class="p">)</span> <span class="o">%</span> <span class="p">{</span>
<a name="cl-225"></a>            <span class="s">&#39;search_fields&#39;</span><span class="p">:</span> <span class="s">&#39;,&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">search_fields</span><span class="p">),</span>
<a name="cl-226"></a>            <span class="s">&#39;admin_media_prefix&#39;</span><span class="p">:</span> <span class="n">admin_media_prefix</span><span class="p">,</span>
<a name="cl-227"></a>            <span class="s">&#39;model_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">rel</span><span class="o">.</span><span class="n">to</span><span class="o">.</span><span class="n">_meta</span><span class="o">.</span><span class="n">module_name</span><span class="p">,</span>
<a name="cl-228"></a>            <span class="s">&#39;app_label&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">rel</span><span class="o">.</span><span class="n">to</span><span class="o">.</span><span class="n">_meta</span><span class="o">.</span><span class="n">app_label</span><span class="p">,</span>
<a name="cl-229"></a>            <span class="s">&#39;label&#39;</span><span class="p">:</span> <span class="n">label</span><span class="p">,</span>
<a name="cl-230"></a>            <span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="n">name</span><span class="p">,</span>
<a name="cl-231"></a>            <span class="s">&#39;extra_params&#39;</span><span class="p">:</span> <span class="n">extra_params</span><span class="p">,</span>
<a name="cl-232"></a>        <span class="p">}</span>
</pre></div>
</td></tr></table>
          </div>
        
      
    
  


  <script id="source-changeset" type="text/html">
  

<a href="/artscoop/django-admin-autocomplete/src/[[raw_node]]/admin_autocomplete_mixin.py?at=default"
   class="[[#selected]]highlight[[/selected]]"
   data-hash="[[node]]">
  [[#author.username]]
    <img class="avatar avatar16" src="[[author.avatar]]"/>
    <span class="author" title="[[raw_author]]">[[author.display_name]]</span>
  [[/author.username]]
  [[^author.username]]
    <img class="avatar avatar16" src="https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/img/default_avatar/16/user_blue.png"/>
    <span class="author unmapped" title="[[raw_author]]">[[author]]</span>
  [[/author.username]]
  <time datetime="[[utctimestamp]]" data-title="true">[[utctimestamp]]</time>
  <span class="message">[[message]]</span>
</a>

</script>


<div class="mask"></div>



  <script id="branch-dialog-template" type="text/html">
  

<div class="tabbed-filter-widget branch-dialog">
  <div class="tabbed-filter">
    <input placeholder="Filter Branches" class="filter-box" autosave="branch-dropdown-1693732" type="text">
    [[^ignoreTags]]
      <div class="aui-tabs horizontal-tabs aui-tabs-disabled filter-tabs">
        <ul class="tabs-menu">
          <li class="menu-item active-tab"><a href="#branches">Branches</a></li>
          <li class="menu-item"><a href="#tags">Tags</a></li>
        </ul>
      </div>
    [[/ignoreTags]]
  </div>
  
    <div class="tab-pane active-pane" id="branches" data-filter-placeholder="Filter Branches">
      <ol class="filter-list">
        <li class="empty-msg">No matching branches</li>
        [[#branches]]
          [[#hasMultipleHeads]]
            [[#heads]]
              <li class="comprev filter-item">
                <a href="/artscoop/django-admin-autocomplete/src/[[changeset]]/admin_autocomplete_mixin.py?at=[[safeName]]" title="[[name]]">
                  [[name]] ([[shortChangeset]])
                </a>
              </li>
            [[/heads]]
          [[/hasMultipleHeads]]
          [[^hasMultipleHeads]]
            <li class="comprev filter-item">
              <a href="/artscoop/django-admin-autocomplete/src/[[changeset]]/admin_autocomplete_mixin.py?at=[[safeName]]" title="[[name]]">
                [[name]]
              </a>
            </li>
          [[/hasMultipleHeads]]
        [[/branches]]
      </ol>
    </div>
    <div class="tab-pane" id="tags" data-filter-placeholder="Filter Tags">
      <ol class="filter-list">
        <li class="empty-msg">No matching tags</li>
        [[#tags]]
          <li class="comprev filter-item">
            <a href="/artscoop/django-admin-autocomplete/src/[[changeset]]/admin_autocomplete_mixin.py?at=[[safeName]]" title="[[name]]">
              [[name]]
            </a>
          </li>
        [[/tags]]
      </ol>
    </div>
  
</div>

</script>



  </div>

  </div>

    </div>
  </div>
  <footer id="footer" role="contentinfo">
    <section class="footer-body">
      <ul>
        <li><a href="http://blog.bitbucket.org">Blog</a></li>
        <li><a href="//bitbucket.org/site/master/issues/new">Report a Bug</a></li>
        <li><a href="/support">Support</a></li>
        <li><a href="http://confluence.atlassian.com/display/BITBUCKET">Documentation</a></li>
        <li><a href="http://confluence.atlassian.com/x/IYBGDQ">API</a></li>
        <li><a href="http://groups.google.com/group/bitbucket-users">Forum</a></li>
        <li><a href="http://status.bitbucket.org/">Server Status</a></li>
        <li><a href="http://www.atlassian.com/hosted/terms.jsp">Terms of Service</a></li>
        <li><a href="http://www.atlassian.com/about/privacy.jsp">Privacy Policy</a></li>
      </ul>
    </section>
  </footer>
</div>

<script type="text/javascript" src="https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/compressed/js/1e3eb202b5f5.js"></script>

<!-- This script exists purely for the benefit of our selenium tests -->
<script>
  setTimeout(function () {
    BB.JsLoaded = true;
  }, 3000);
</script>



<script>
  (function (window) {
    BB.images = {
      invitation: 'https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/img/icons/fugue/card_address.png',
      noAvatar: 'https://dwz7u9t8u8usb.cloudfront.net/m/a1fb05d05bb7/img/default_avatar/16/user_blue.png'
    };
    BB.user = {"username": "artscoop", "displayName": "artscoop", "firstName": "", "avatarUrl": "https://secure.gravatar.com/avatar/2ac66487401fecdb194f7a0ae07dd8fd?d=https%3A%2F%2Fdwz7u9t8u8usb.cloudfront.net%2Fm%2Fa1fb05d05bb7%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png\u0026s=32", "lastName": "", "isTeam": false, "isSshEnabled": false, "isKbdShortcutsEnabled": true, "id": 485789, "isAuthenticated": true};
    BB.repo || (BB.repo = {});
    
      BB.repo.id = 1693732;
      
      
        BB.repo.language = null;
        BB.repo.pygmentsLanguage = null;
      
      
        BB.repo.slug = 'django\u002Dadmin\u002Dautocomplete';
      
      
        BB.repo.owner = {};
        BB.repo.owner.username = 'artscoop';
      
      // Coerce `BB.repo` to a string to get
      // "davidchambers/mango" or whatever.
      BB.repo.toString = function () {
        return BB.cname ? this.slug : '{owner.username}/{slug}'.format(this);
      }
      
        BB.changeset = 'b26a9604d6429037f8b9b95906bb607ac6fe7951'
      
      
    
    window.setInterval(BB.localize, 60 * 1000);
    BB.localize();

  })(window);
</script>



<script>
    // Bitbucket Google Analytics
    (function (window) {
        // Track the main pageview to the Bitbucket GA account.
        BB.gaqPush(['_trackPageview']);
        // Track the main pageview to the Atlassian GA account.
        BB.gaqPush(['atl._trackPageview']);

        


        

        // Include GA commands from sub-templates
        

        (function () {
            var ga = document.createElement('script');
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            ga.setAttribute('async', 'true');
            document.documentElement.firstChild.appendChild(ga);
        }());
    })(window);
</script>




</body>
</html>
