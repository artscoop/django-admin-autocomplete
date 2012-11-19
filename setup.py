<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>
  artscoop / django-admin-autocomplete 
  / source  / setup.py
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
        
          <a href="/artscoop/django-admin-autocomplete/src/b26a9604d642/setup.py?at=default"
             class="aui-button aui-style pjax-trigger active">
            Source
          </a>
          <a href="/artscoop/django-admin-autocomplete/diff/setup.py?diff2=b26a9604d642&at=default"
             class="aui-button aui-style pjax-trigger "
             title="Diff to previous change">
            Diff
          </a>
          <a href="/artscoop/django-admin-autocomplete/history-node/b26a9604d642/setup.py?at=default"
             class="aui-button aui-style pjax-trigger ">
            History
          </a>
        
      </div>
    </div>
  
  <h1>
    <a href="/artscoop/django-admin-autocomplete/src/b26a9604d642?at=default"
       class="pjax-trigger" title="[u&#39;setup.py&#39;]">django-admin-autocomplete</a> /
    
      
        
          <span>setup.py</span>
        
      
    
  </h1>
  
    
    
  
  <div class="clearfix"></div>
</header>


  
    <div id="source-view">
      <div class="toolbar">
        <div class="primary">
          <div class="aui-buttons">
            
              <button id="file-history-trigger" class="aui-button aui-style changeset-info"
                      data-changeset="b26a9604d6429037f8b9b95906bb607ac6fe7951"
                      data-path="setup.py"
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
                <a href="/artscoop/django-admin-autocomplete/annotate/b26a9604d6429037f8b9b95906bb607ac6fe7951/setup.py?at=default"
                   class="aui-button aui-style pjax-trigger">Blame</a>
              </div>
            
            <div class="aui-buttons">
              
              <a href="/artscoop/django-admin-autocomplete/full-commit/b26a9604d642/setup.py" class="aui-button aui-style"
                 title="View full commit b26a960">Full Commit</a>
              
                <a id="embed-link" href="/artscoop/django-admin-autocomplete/src/b26a9604d6429037f8b9b95906bb607ac6fe7951/setup.py?embed=t"
                   class="aui-button aui-style">Embed</a>
              
              <a href="/artscoop/django-admin-autocomplete/raw/b26a9604d6429037f8b9b95906bb607ac6fe7951/setup.py"
                 class="aui-button aui-style">Raw</a>
            </div>
          </div>
        <div class="clearfix"></div>
      </div>
    </div>

    
      
        
          <div class="file-source">
            <table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#cl-1"> 1</a>
<a href="#cl-2"> 2</a>
<a href="#cl-3"> 3</a>
<a href="#cl-4"> 4</a>
<a href="#cl-5"> 5</a>
<a href="#cl-6"> 6</a>
<a href="#cl-7"> 7</a>
<a href="#cl-8"> 8</a>
<a href="#cl-9"> 9</a>
<a href="#cl-10">10</a>
<a href="#cl-11">11</a>
<a href="#cl-12">12</a>
<a href="#cl-13">13</a>
<a href="#cl-14">14</a>
<a href="#cl-15">15</a>
<a href="#cl-16">16</a>
<a href="#cl-17">17</a>
<a href="#cl-18">18</a>
<a href="#cl-19">19</a>
<a href="#cl-20">20</a>
<a href="#cl-21">21</a>
<a href="#cl-22">22</a>
<a href="#cl-23">23</a>
<a href="#cl-24">24</a>
<a href="#cl-25">25</a></pre></div></td><td class="code"><div class="highlight"><pre><a name="cl-1"></a><span class="c">#!/usr/bin/env python</span>
<a name="cl-2"></a>
<a name="cl-3"></a><span class="kn">from</span> <span class="nn">distutils.core</span> <span class="kn">import</span> <span class="n">setup</span>
<a name="cl-4"></a>
<a name="cl-5"></a><span class="n">setup</span><span class="p">(</span>
<a name="cl-6"></a>    <span class="n">name</span> <span class="o">=</span> <span class="s">&quot;Django Autocomplete Mixin&quot;</span><span class="p">,</span>
<a name="cl-7"></a>    <span class="n">version</span> <span class="o">=</span> <span class="s">&#39;0.2&#39;</span><span class="p">,</span>
<a name="cl-8"></a>    <span class="n">install_requires</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;django&gt;=1.0&#39;</span><span class="p">],</span>
<a name="cl-9"></a>    <span class="n">author</span> <span class="o">=</span> <span class="s">&quot;Tim Babych&quot;</span><span class="p">,</span>
<a name="cl-10"></a>    <span class="n">author_email</span> <span class="o">=</span> <span class="s">&quot;tim.babych@gmail.com&quot;</span><span class="p">,</span>
<a name="cl-11"></a>    <span class="n">description</span> <span class="o">=</span> <span class="s">&quot;Mixin for turning foreignKey fields into autocomplete lookups.&quot;</span><span class="p">,</span>
<a name="cl-12"></a>    <span class="n">keywords</span> <span class="o">=</span> <span class="s">&quot;google, django, autocomplete&quot;</span><span class="p">,</span>
<a name="cl-13"></a>    <span class="n">url</span> <span class="o">=</span> <span class="s">&quot;https://bitbucket.org/tymofiy/django-admin-autocomplete&quot;</span><span class="p">,</span>
<a name="cl-14"></a>    <span class="n">py_modules</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;admin_autocomplete_mixin&#39;</span><span class="p">],</span>
<a name="cl-15"></a>    <span class="n">classifiers</span><span class="o">=</span><span class="p">[</span>
<a name="cl-16"></a>        <span class="s">&quot;Development Status :: 3 - Alpha&quot;</span><span class="p">,</span>
<a name="cl-17"></a>        <span class="s">&quot;Environment :: Web Environment&quot;</span><span class="p">,</span>
<a name="cl-18"></a>        <span class="s">&quot;Framework :: Django&quot;</span><span class="p">,</span>
<a name="cl-19"></a>        <span class="s">&quot;Intended Audience :: Developers&quot;</span><span class="p">,</span>
<a name="cl-20"></a>        <span class="s">&quot;Programming Language :: Python&quot;</span><span class="p">,</span>
<a name="cl-21"></a>        <span class="s">&quot;License :: OSI Approved :: BSD License&quot;</span><span class="p">,</span>
<a name="cl-22"></a>        <span class="s">&quot;Operating System :: OS Independent&quot;</span><span class="p">,</span>
<a name="cl-23"></a>        <span class="s">&quot;Topic :: Software Development&quot;</span>
<a name="cl-24"></a>    <span class="p">],</span>
<a name="cl-25"></a><span class="p">)</span>
</pre></div>
</td></tr></table>
          </div>
        
      
    
  


  <script id="source-changeset" type="text/html">
  

<a href="/artscoop/django-admin-autocomplete/src/[[raw_node]]/setup.py?at=default"
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
                <a href="/artscoop/django-admin-autocomplete/src/[[changeset]]/setup.py?at=[[safeName]]" title="[[name]]">
                  [[name]] ([[shortChangeset]])
                </a>
              </li>
            [[/heads]]
          [[/hasMultipleHeads]]
          [[^hasMultipleHeads]]
            <li class="comprev filter-item">
              <a href="/artscoop/django-admin-autocomplete/src/[[changeset]]/setup.py?at=[[safeName]]" title="[[name]]">
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
            <a href="/artscoop/django-admin-autocomplete/src/[[changeset]]/setup.py?at=[[safeName]]" title="[[name]]">
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
